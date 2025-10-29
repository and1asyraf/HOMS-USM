# How to Run the Hostel Complaint Management System

## Quick Start Guide

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Access the Application
- Open your web browser
- Go to: `http://localhost:5000`

### Step 4: Create Admin Account (First Time Only)
- Visit: `http://localhost:5000/create_admin`
- Default admin login: `admin@hostel.com` / `admin123`

## What You Can Do

### As a Student:
1. **Register** - Create account with your hostel details
2. **Login** - Access your dashboard
3. **Submit Complaints** - Report facility issues with photos
4. **Track Status** - See if your complaint is Pending/In Progress/Resolved
5. **Give Feedback** - Rate and comment on resolved complaints

### As an Admin:
1. **Login** - Use admin credentials
2. **View All Complaints** - See complaints from all students
3. **Filter** - Search by status, hostel, or category
4. **Update Status** - Change complaint status as work progresses
5. **View Feedback** - See student ratings and comments

## Troubleshooting

**Port Already in Use?**
- Change port in `app.py`: `app.run(debug=True, port=5001)`

**Database Issues?**
- Delete `hostel_complaints.db` and restart

**Permission Errors?**
- Run as administrator (Windows)

## Features Included
- ✅ Student registration and login
- ✅ Complaint submission with image uploads
- ✅ Admin dashboard for managing complaints
- ✅ Status tracking (Pending → In Progress → Resolved)
- ✅ Feedback system with star ratings
- ✅ Responsive design for mobile/desktop
- ✅ Filter and search functionality

## File Structure
```
├── app.py              # Main application
├── models.py           # Database models
├── requirements.txt    # Dependencies
├── static/            # CSS, JS, uploads
└── templates/         # HTML templates
```

That's it! The app is ready to use for managing hostel complaints and feedback.
