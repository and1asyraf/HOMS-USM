from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from models import db, User, Complaint, Feedback

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hostel_complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize database
db.init_app(app)

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Allowed file extensions for image uploads
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    """Decorator to require login for protected routes"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    """Decorator to require admin role for protected routes"""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('index'))
        user = User.query.get(session['user_id'])
        if not user or user.role != 'admin':
            flash('Admin access required.', 'error')
            return redirect(url_for('student_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    """Home page with login/register forms"""
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('student_dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    """Handle user registration"""
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    hostel = request.form.get('hostel')
    room_no = request.form.get('room_no')
    
    # Validate required fields
    if not all([name, email, password, hostel, room_no]):
        flash('All fields are required.', 'error')
        return redirect(url_for('index'))
    
    # Check if email already exists
    if User.query.filter_by(email=email).first():
        flash('Email already registered.', 'error')
        return redirect(url_for('index'))
    
    # Create new user
    hashed_password = generate_password_hash(password)
    user = User(
        name=name,
        email=email,
        password=hashed_password,
        hostel=hostel,
        room_no=room_no,
        role='student'
    )
    
    try:
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Registration failed. Please try again.', 'error')
    
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    """Handle user login"""
    email = request.form.get('email')
    password = request.form.get('password')
    
    if not email or not password:
        flash('Email and password are required.', 'error')
        return redirect(url_for('index'))
    
    user = User.query.filter_by(email=email).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id
        session['user_name'] = user.name
        session['user_role'] = user.role
        
        if user.role == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('student_dashboard'))
    else:
        flash('Invalid email or password.', 'error')
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    """Handle user logout"""
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/student_dashboard')
@login_required
def student_dashboard():
    """Student dashboard showing complaints and submission form"""
    user = User.query.get(session['user_id'])
    if user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    
    # Get user's complaints
    complaints = Complaint.query.filter_by(user_id=user.id).order_by(Complaint.created_at.desc()).all()
    
    return render_template('student_dashboard.html', user=user, complaints=complaints)

@app.route('/submit_complaint', methods=['POST'])
@login_required
def submit_complaint():
    """Handle complaint submission"""
    user = User.query.get(session['user_id'])
    if user.role == 'admin':
        return redirect(url_for('admin_dashboard'))
    
    category = request.form.get('category')
    description = request.form.get('description')
    
    if not category or not description:
        flash('Category and description are required.', 'error')
        return redirect(url_for('student_dashboard'))
    
    # Handle file upload
    image_path = None
    if 'image' in request.files:
        file = request.files['image']
        if file and file.filename and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # Add timestamp to avoid filename conflicts
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
            filename = timestamp + filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            image_path = filename
    
    # Create complaint
    complaint = Complaint(
        user_id=user.id,
        category=category,
        description=description,
        image_path=image_path,
        status='Pending'
    )
    
    try:
        db.session.add(complaint)
        db.session.commit()
        flash('Complaint submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to submit complaint. Please try again.', 'error')
    
    return redirect(url_for('student_dashboard'))

@app.route('/admin_dashboard')
@admin_required
def admin_dashboard():
    """Admin dashboard for managing complaints"""
    # Get filter parameters
    status_filter = request.args.get('status', '')
    hostel_filter = request.args.get('hostel', '')
    category_filter = request.args.get('category', '')
    
    # Build query
    query = Complaint.query
    
    if status_filter:
        query = query.filter(Complaint.status == status_filter)
    if hostel_filter:
        query = query.join(User).filter(User.hostel == hostel_filter)
    if category_filter:
        query = query.filter(Complaint.category == category_filter)
    
    complaints = query.order_by(Complaint.created_at.desc()).all()
    
    # Get unique values for filter dropdowns
    all_hostels = db.session.query(User.hostel).distinct().all()
    all_categories = db.session.query(Complaint.category).distinct().all()
    
    return render_template('admin_dashboard.html', 
                         complaints=complaints,
                         all_hostels=[h[0] for h in all_hostels],
                         all_categories=[c[0] for c in all_categories],
                         current_filters={
                             'status': status_filter,
                             'hostel': hostel_filter,
                             'category': category_filter
                         })

@app.route('/update_status', methods=['POST'])
@admin_required
def update_status():
    """Update complaint status"""
    complaint_id = request.form.get('complaint_id')
    new_status = request.form.get('status')
    
    if not complaint_id or not new_status:
        flash('Invalid request.', 'error')
        return redirect(url_for('admin_dashboard'))
    
    complaint = Complaint.query.get(complaint_id)
    if not complaint:
        flash('Complaint not found.', 'error')
        return redirect(url_for('admin_dashboard'))
    
    complaint.status = new_status
    
    try:
        db.session.commit()
        flash(f'Status updated to {new_status}.', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to update status.', 'error')
    
    return redirect(url_for('admin_dashboard'))

@app.route('/feedback/<int:complaint_id>')
@login_required
def feedback_form(complaint_id):
    """Show feedback form for resolved complaint"""
    user = User.query.get(session['user_id'])
    complaint = Complaint.query.get(complaint_id)
    
    if not complaint:
        flash('Complaint not found.', 'error')
        return redirect(url_for('student_dashboard'))
    
    # Check if user owns this complaint
    if complaint.user_id != user.id:
        flash('You can only provide feedback for your own complaints.', 'error')
        return redirect(url_for('student_dashboard'))
    
    # Check if complaint is resolved
    if complaint.status != 'Resolved':
        flash('You can only provide feedback for resolved complaints.', 'error')
        return redirect(url_for('student_dashboard'))
    
    # Check if feedback already exists
    existing_feedback = Feedback.query.filter_by(complaint_id=complaint_id).first()
    
    return render_template('feedback.html', complaint=complaint, existing_feedback=existing_feedback)

@app.route('/submit_feedback', methods=['POST'])
@login_required
def submit_feedback():
    """Handle feedback submission"""
    user = User.query.get(session['user_id'])
    complaint_id = request.form.get('complaint_id')
    rating = request.form.get('rating')
    comment = request.form.get('comment')
    
    if not complaint_id or not rating:
        flash('Rating is required.', 'error')
        return redirect(url_for('feedback_form', complaint_id=complaint_id))
    
    complaint = Complaint.query.get(complaint_id)
    if not complaint or complaint.user_id != user.id:
        flash('Invalid complaint.', 'error')
        return redirect(url_for('student_dashboard'))
    
    # Check if feedback already exists
    existing_feedback = Feedback.query.filter_by(complaint_id=complaint_id).first()
    
    if existing_feedback:
        # Update existing feedback
        existing_feedback.rating = int(rating)
        existing_feedback.comment = comment
        existing_feedback.submitted_at = datetime.now()
    else:
        # Create new feedback
        feedback = Feedback(
            complaint_id=int(complaint_id),
            rating=int(rating),
            comment=comment
        )
        db.session.add(feedback)
    
    try:
        db.session.commit()
        flash('Feedback submitted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to submit feedback.', 'error')
    
    return redirect(url_for('student_dashboard'))

@app.route('/create_admin')
def create_admin():
    """Create admin user (for initial setup)"""
    # Check if admin already exists
    if User.query.filter_by(role='admin').first():
        flash('Admin user already exists.', 'info')
        return redirect(url_for('index'))
    
    # Create admin user
    admin = User(
        name='Admin',
        email='admin@hostel.com',
        password=generate_password_hash('admin123'),
        hostel='Admin Block',
        room_no='A001',
        role='admin'
    )
    
    try:
        db.session.add(admin)
        db.session.commit()
        flash('Admin user created! Email: admin@hostel.com, Password: admin123', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Failed to create admin user.', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
