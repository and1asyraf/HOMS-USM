from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """User model for students and admins"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    hostel = db.Column(db.String(100), nullable=False)
    room_no = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='student')  # 'student' or 'admin'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with complaints
    complaints = db.relationship('Complaint', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<User {self.name}>'

class Complaint(db.Model):
    """Complaint model for hostel facility issues"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)  # e.g., 'Electrical', 'Plumbing', 'WiFi', etc.
    description = db.Column(db.Text, nullable=False)
    image_path = db.Column(db.String(200), nullable=True)  # Optional image attachment
    status = db.Column(db.String(20), nullable=False, default='Pending')  # 'Pending', 'In Progress', 'Resolved'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with feedback
    feedback = db.relationship('Feedback', backref='complaint', lazy=True, uselist=False)
    
    def __repr__(self):
        return f'<Complaint {self.id} - {self.category}>'

class Feedback(db.Model):
    """Feedback model for resolved complaints"""
    id = db.Column(db.Integer, primary_key=True)
    complaint_id = db.Column(db.Integer, db.ForeignKey('complaint.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # 1-5 star rating
    comment = db.Column(db.Text, nullable=True)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Feedback {self.id} - Rating: {self.rating}>'
