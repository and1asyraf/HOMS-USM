# Hostel Facilities Complaint and Feedback Management System

A complete web application for managing hostel facility complaints and feedback, built with Flask and SQLite.

## 🚀 Quick Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd hostel-complaints
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and go to: `http://localhost:5000`
   - Create an admin account by visiting: `http://localhost:5000/create_admin`
   - Default admin credentials: `admin@hostel.com` / `admin123`

## 📁 Project Structure

```
hostel-complaints/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── static/
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   ├── js/
│   │   └── main.js     # JavaScript functionality
│   └── uploads/        # Image uploads (created automatically)
└── templates/
    ├── base.html       # Base template
    ├── login.html      # Login/Register page
    ├── student_dashboard.html  # Student interface
    ├── admin_dashboard.html    # Admin interface
    └── feedback.html   # Feedback form
```

## 🎯 Features

### Student Features
- **Registration & Login**: Secure authentication system
- **Submit Complaints**: Report issues with categories and optional images
- **Track Status**: View complaint status (Pending/In Progress/Resolved)
- **Provide Feedback**: Rate and comment on resolved complaints

### Admin Features
- **Manage Complaints**: View all submitted complaints
- **Filter System**: Filter by status, hostel, or category
- **Update Status**: Change complaint status through workflow
- **View Feedback**: See student ratings and comments

## 🗄️ Database Schema

The application uses SQLite with three main tables:

- **users**: Student and admin accounts
- **complaints**: Facility issue reports
- **feedback**: Student ratings and comments

## 🔧 Configuration

### Environment Variables
You can customize the application by modifying these settings in `app.py`:

```python
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
```

### File Uploads
- Supported image formats: JPG, PNG, GIF
- Maximum file size: 16MB
- Images are stored in `static/uploads/` directory

## 🎨 Customization

### Styling
- Modify `static/css/style.css` for custom styling
- The design is responsive and works on mobile devices
- Uses modern CSS with Flexbox and Grid layouts

### Categories
Add new complaint categories by modifying the select options in `student_dashboard.html`:

```html
<option value="NewCategory">New Category Name</option>
```

## 🚨 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Change port in app.py
   app.run(debug=True, port=5001)
   ```

2. **Database errors**
   ```bash
   # Delete database file and restart
   rm hostel_complaints.db
   python app.py
   ```

3. **Permission errors (Windows)**
   ```bash
   # Run as administrator or change upload folder permissions
   ```

4. **Module not found errors**
   ```bash
   # Ensure virtual environment is activated
   pip install -r requirements.txt
   ```

### Debug Mode
The application runs in debug mode by default. For production:
- Set `debug=False` in `app.py`
- Use a proper secret key
- Configure a production database

## 📝 Usage Guide

### For Students
1. Register with your hostel details
2. Login to access your dashboard
3. Submit complaints with detailed descriptions
4. Upload images if helpful
5. Track complaint status
6. Provide feedback when resolved

### For Admins
1. Login with admin credentials
2. View all complaints in the dashboard
3. Use filters to find specific complaints
4. Update status as work progresses
5. View student feedback for resolved issues

## 🔒 Security Notes

- Passwords are hashed using Werkzeug's security functions
- File uploads are validated for type and size
- SQL injection protection via SQLAlchemy ORM
- Session-based authentication

## 📚 Academic Use

This project is designed for educational purposes and includes:
- Clean, commented code
- Modern web development practices
- Responsive design principles
- Database relationship modeling
- User authentication and authorization

## 🤝 Contributing

This is an academic project. Feel free to:
- Add new features
- Improve the UI/UX
- Fix bugs
- Add more validation
- Enhance security

## 📄 License

This project is created for academic purposes. Feel free to use and modify for educational use.

---

**Note**: This is a development version designed for localhost use. For production deployment, additional security measures and configuration would be required.
