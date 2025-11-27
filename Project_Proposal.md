# Project Proposal: Hostel Facilities Complaint and Feedback Management System

## Table of Contents
1. [Introduction](#1-introduction)
2. [Stakeholders](#2-stakeholders)
3. [Category of Web Application](#3-category-of-web-application)
4. [Web Application Modelling](#4-web-application-modelling)
5. [Prototype Design](#5-prototype-design)
6. [Architecture Design](#6-architecture-design)

---

## 1. Introduction

### 1.1 Project Overview

The **Hostel Facilities Complaint and Feedback Management System** is a web-based application designed to streamline the process of reporting, tracking, and resolving facility-related issues in university hostels. Traditional methods of physical complaint submission are inefficient, time-consuming, and often lead to communication gaps between students and hostel administration.

This system provides a centralized digital platform where students can easily submit complaints about faulty facilities (such as broken fans, leaking pipes, poor Wi-Fi connectivity, furniture issues, security concerns, etc.), track the status of their complaints in real-time, and provide feedback after issue resolution. Simultaneously, administrators can efficiently manage complaints, update their status, and monitor feedback to improve service quality.

### 1.2 Problem Statement

University hostels accommodate hundreds of students who face various facility-related problems on a daily basis. The current manual complaint management system suffers from:

- **Inefficiency**: Physical complaint submission requires students to visit administration offices during specific hours
- **Lack of Transparency**: Students have no visibility into complaint status or resolution progress
- **Poor Documentation**: Physical records are prone to loss and difficult to track
- **Delayed Response**: Communication gaps lead to delayed issue resolution
- **No Feedback Mechanism**: There is no systematic way to collect student feedback on resolved issues
- **Resource Wastage**: Manual tracking consumes significant administrative resources

### 1.3 Solution

Our web application addresses these challenges by providing:

- **24/7 Online Access**: Students can submit complaints anytime from any device
- **Real-time Status Tracking**: Clear visibility into complaint status (Pending → In Progress → Resolved)
- **Digital Documentation**: All complaints are digitally stored with optional image attachments
- **Streamlined Workflow**: Automated status updates and notifications
- **Feedback System**: Structured rating and comment system for quality improvement
- **Administrative Dashboard**: Comprehensive management interface with filtering and search capabilities

### 1.4 Core Functionalities

1. **User Authentication & Registration**
   - Student registration with hostel and room details
   - Secure login system with session management
   - Role-based access control (Student/Admin)

2. **Complaint Submission**
   - Categorized complaint forms (Electrical, Plumbing, WiFi, Furniture, Security, Cleaning, Other)
   - Detailed description fields
   - Optional image upload support (JPG, PNG, GIF up to 16MB)
   - Timestamp tracking

3. **Complaint Management (Admin)**
   - View all complaints in a centralized dashboard
   - Filter complaints by status, hostel, or category
   - Update complaint status through workflow stages
   - View complaint details with student information

4. **Status Tracking (Student)**
   - Real-time complaint status visibility
   - Personal dashboard showing all submitted complaints
   - Status indicators (Pending, In Progress, Resolved)

5. **Feedback System**
   - Submit feedback only for resolved complaints
   - 5-star rating system
   - Optional comment submission
   - View feedback history (for updates)

---

## 2. Stakeholders

### 2.1 Primary Stakeholders

#### **Students (End Users)**
- **Role**: Primary beneficiaries who submit complaints and provide feedback
- **Needs**: 
  - Easy and quick complaint submission
  - Transparency in complaint processing
  - Quick resolution of facility issues
  - Convenient feedback mechanism
- **Benefits**: 
  - 24/7 complaint submission capability
  - Real-time status tracking
  - Improved living conditions through faster issue resolution

#### **Hostel Administrators (System Managers)**
- **Role**: Manage and resolve complaints, maintain facility standards
- **Needs**:
  - Centralized complaint management system
  - Efficient workflow for complaint processing
  - Access to student feedback for quality improvement
  - Reporting and filtering capabilities
- **Benefits**:
  - Reduced administrative overhead
  - Better resource allocation
  - Data-driven decision making
  - Improved service quality tracking

### 2.2 Secondary Stakeholders

#### **University IT Department**
- **Role**: System maintenance and technical support
- **Needs**: Scalable, maintainable system architecture
- **Benefits**: Standard web technologies, easy to maintain

#### **Maintenance Staff**
- **Role**: Physical resolution of complaints
- **Needs**: Access to complaint details and priorities
- **Benefits**: Clear work assignments, better planning

#### **University Management**
- **Role**: Strategic oversight and quality assurance
- **Needs**: Overall system performance metrics
- **Benefits**: Improved student satisfaction, operational efficiency

---

## 3. Category of Web Application

### 3.1 Application Type

**Category**: **Business-to-Administration (B2A) Web Application**

This application falls under the category of **Institutional Management System** or **Service Management System**, specifically designed for educational institutions.

### 3.2 Application Classification

- **Interaction Pattern**: **Multi-user, Role-based Web Application**
- **Architecture Pattern**: **Client-Server Architecture** (3-tier architecture)
- **Deployment Model**: **Web-based Application** (Browser-accessible)
- **Primary Function**: **Transaction Processing System** and **Information Management System**

### 3.3 Technical Classification

- **Technology Stack**: **Server-side Rendered Web Application** (SSR)
- **Framework**: Flask (Python) - Lightweight WSGI framework
- **Database**: SQLite (Relational Database Management System)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Communication**: HTTP/HTTPS protocol

### 3.4 Application Domain

- **Domain**: Educational Institution - Hostel Facility Management
- **Industry**: Higher Education Administration
- **Purpose**: Internal Operations Management
- **Scope**: Single Institution (Designed for university-level deployment)

---

## 4. Web Application Modelling

### 4.1 User Diagram

#### System Actors and Roles

```
┌─────────────────────────────────────────────────────────┐
│                   SYSTEM ACTORS                         │
└─────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────┐
│   Student    │         │  Administrator│
│  (End User)  │         │  (System      │
│              │         │   Manager)     │
└──────┬───────┘         └──────┬───────┘
       │                        │
       │                        │
       └──────────┬─────────────┘
                  │
        ┌─────────▼──────────┐
        │   Hostel Complaint │
        │  Management System  │
        └────────────────────┘
```

**Actor Descriptions:**

1. **Student**
   - Can register and create account
   - Can login and access personal dashboard
   - Can submit new complaints
   - Can view own complaint history
   - Can track complaint status
   - Can provide feedback for resolved complaints

2. **Administrator**
   - Can login with admin credentials
   - Can view all complaints from all students
   - Can filter complaints by various criteria
   - Can update complaint status
   - Can view student feedback
   - Can manage system data

### 4.2 Use Case Diagram

```
                         ┌─────────────────────┐
                         │  Complaint          │
                         │  Management System   │
                         └─────────────────────┘
                                    │
        ┌───────────────────────────┼──────────────────────────┐
        │                           │                           │
        ▼                           ▼                           ▼
┌───────────────┐         ┌──────────────────┐       ┌──────────────┐
│   Student     │         │  Administrator    │       │   System      │
│   Use Cases   │         │    Use Cases      │       │   Functions   │
└───────────────┘         └──────────────────┘       └──────────────┘

┌───────────────────┐    ┌───────────────────┐    ┌───────────────┐
│ Register Account  │    │ Login             │    │ Create Admin   │
│ Login             │    │ View All          │    │                │
│ Submit Complaint  │    │  Complaints       │    │                │
│ View Complaints   │    │ Filter Complaints │    │                │
│ Track Status      │    │ Update Status     │    │                │
│ Upload Image      │    │ View Feedback     │    │                │
│ Provide Feedback  │    │ Manage Workflow   │    │                │
└───────────────────┘    └──────────────────┘    └───────────────┘
```

**Detailed Use Cases:**

**Student Use Cases:**
1. **UC-001: Register Account** - Create new student account with hostel details
2. **UC-002: Login** - Authenticate and access personal dashboard
3. **UC-003: Submit Complaint** - Create new complaint with category, description, and optional image
4. **UC-004: View Own Complaints** - Access personal complaint history
5. **UC-005: Track Complaint Status** - Monitor status changes
6. **UC-006: Upload Image** - Attach image file with complaint
7. **UC-007: Provide Feedback** - Submit rating and comment for resolved complaints

**Administrator Use Cases:**
1. **UC-008: Admin Login** - Authenticate with admin credentials
2. **UC-009: View All Complaints** - Access complete complaint database
3. **UC-010: Filter Complaints** - Search by status, hostel, or category
4. **UC-011: Update Complaint Status** - Change status (Pending → In Progress → Resolved)
5. **UC-012: View Feedback** - Access student ratings and comments
6. **UC-013: Manage Workflow** - Process complaints through resolution

### 4.3 Class Diagram

```
┌──────────────────────────────────────────────────────────────┐
│                      CLASS DIAGRAM                           │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────┐
│         User             │
├──────────────────────────┤
│ - id: Integer (PK)       │
│ - name: String           │
│ - email: String (UNIQUE) │
│ - password: String       │
│ - hostel: String         │
│ - room_no: String        │
│ - role: String           │
│ - created_at: DateTime   │
├──────────────────────────┤
│ + register()             │
│ + login()                │
│ + logout()               │
└───────────┬──────────────┘
            │ 1
            │
            │ *
            ▼
┌──────────────────────────┐
│       Complaint          │
├──────────────────────────┤
│ - id: Integer (PK)       │
│ - user_id: Integer (FK)  │
│ - category: String       │
│ - description: Text       │
│ - image_path: String     │
│ - status: String         │
│ - created_at: DateTime   │
├──────────────────────────┤
│ + submit()               │
│ + updateStatus()         │
│ + getStatus()            │
└───────────┬──────────────┘
            │ 1
            │
            │ 0..1
            ▼
┌──────────────────────────┐
│        Feedback          │
├──────────────────────────┤
│ - id: Integer (PK)       │
│ - complaint_id: Integer  │
│          (FK)            │
│ - rating: Integer         │
│ - comment: Text          │
│ - submitted_at: DateTime │
├──────────────────────────┤
│ + submit()               │
│ + update()               │
│ + getRating()            │
└──────────────────────────┘

┌──────────────────────────┐
│    Flask Application     │
├──────────────────────────┤
│ - app: Flask             │
│ - db: SQLAlchemy         │
│ - session: Session       │
├──────────────────────────┤
│ + login_required()       │
│ + admin_required()       │
│ + allowed_file()        │
└──────────────────────────┘
```

**Class Relationships:**

1. **User → Complaint**: One-to-Many relationship (One user can have many complaints)
2. **Complaint → Feedback**: One-to-One relationship (One complaint can have one feedback)
3. **Complaint → User**: Many-to-One relationship (Many complaints belong to one user)
4. **Feedback → Complaint**: One-to-One relationship (One feedback belongs to one complaint)

### 4.4 Sequence Diagram: Complaint Submission Process

```
┌──────────────────────────────────────────────────────────────────────┐
│           SEQUENCE DIAGRAM: COMPLAINT SUBMISSION                     │
└──────────────────────────────────────────────────────────────────────┘

Student         Browser        Flask App        Database        File System
  │                │               │                │                 │
  │   [Login]      │               │                │                 │
  │───────────────>│               │                │                 │
  │                │  POST /login  │               │                 │
  │                │──────────────>│               │                 │
  │                │               │ Verify User    │                 │
  │                │               │───────────────>│                 │
  │                │               │ User Data      │                 │
  │                │               │<───────────────│                 │
  │                │ Session       │                │                 │
  │                │<──────────────│                │                 │
  │   Dashboard    │               │                │                 │
  │<───────────────│               │                │                 │
  │                │               │                │                 │
  │  [Submit Form] │               │                │                 │
  │───────────────>│               │                │                 │
  │                │ POST /submit  │                │                 │
  │                │  _complaint   │                │                 │
  │                │──────────────>│                │                 │
  │                │               │ Validate Data  │                 │
  │                │               │                │                 │
  │                │               │ Save Image     │                 │
  │                │               │─────────────────────────────────>│
  │                │               │                │                 │
  │                │               │ Create         │                 │
  │                │               │ Complaint      │                 │
  │                │               │───────────────>│                 │
  │                │               │                │ Save Record     │
  │                │               │ Success        │                 │
  │                │               │<───────────────│                 │
  │                │ Redirect      │                │                 │
  │                │<──────────────│                │                 │
  │   Updated      │               │                │                 │
  │   Dashboard    │               │                │                 │
  │<───────────────│               │                │                 │
```

**Sequence Flow Explanation:**

1. **Authentication Phase**:
   - Student submits login credentials through browser
   - Flask app validates credentials against database
   - Session is created and maintained

2. **Complaint Submission Phase**:
   - Student fills complaint form with details
   - Form data sent to Flask application via POST request
   - Application validates input data
   - If image provided, file is saved to file system
   - Complaint object is created and persisted to database

3. **Response Phase**:
   - Database confirms successful save
   - Flask application redirects to dashboard
   - Updated dashboard displays new complaint

### 4.5 Entity Relationship Diagram (ERD)

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│    User     │          │  Complaint   │          │  Feedback   │
├─────────────┤          ├──────────────┤          ├─────────────┤
│ id (PK)     │          │ id (PK)     │          │ id (PK)     │
│ name        │          │ user_id (FK) │◄─────────│complaint_id │
│ email       │          │ category     │    1     │    (FK)     │
│ password    │          │ description  │          │ rating      │
│ hostel      │          │ image_path   │          │ comment     │
│ room_no     │          │ status       │          │submitted_at │
│ role        │          │ created_at   │          │             │
│ created_at  │          │              │          │             │
└──────┬──────┘          └──────────────┘          └─────────────┘
       │
       │ *
       │
       │
   One User can have
   Multiple Complaints
```

**Relationships:**
- **User → Complaint**: One-to-Many (1:N)
- **Complaint → Feedback**: One-to-One (1:1)

---

## 5. Prototype Design

### 5.1 Login/Registration Page

**Design Elements:**
- Clean, modern interface with glass-morphism design
- Tab-based navigation between Login and Registration
- Input fields for:
  - Email and Password (Login)
  - Name, Email, Password, Hostel Name, Room Number (Registration)
- Gradient button styling
- Responsive layout for mobile and desktop

**Functionality:**
- Form validation
- Error message display
- Success notifications
- Session management

### 5.2 Student Dashboard

**Layout:**
- Two-column grid layout
- Left column: Complaint submission form
- Right column: List of submitted complaints

**Complaint Form Features:**
- Category dropdown (Electrical, Plumbing, WiFi, Furniture, Security, Cleaning, Other)
- Description textarea
- Image upload button with preview
- Submit button with loading state

**Complaint List Features:**
- Status badges (color-coded: Pending, In Progress, Resolved)
- Complaint details with timestamps
- Image preview link
- Feedback button for resolved complaints
- Scrollable list for multiple complaints

### 5.3 Admin Dashboard

**Layout:**
- Full-width layout with filter section
- Comprehensive complaint management table

**Filter Section:**
- Status dropdown filter
- Hostel dropdown filter
- Category dropdown filter
- Clear filters button

**Complaint Management Table:**
- All complaint details displayed
- Student information (name, hostel, room number)
- Status update dropdown with update button
- Feedback display for resolved complaints
- Visual separation between complaints

### 5.4 Feedback Page

**Layout:**
- Centered card design
- Complaint summary section
- Rating input (5-star system)
- Comment textarea
- Submit/Update button

**Features:**
- Star rating selection with visual feedback
- Display of previous feedback if updating
- Back to dashboard button

### 5.5 Design Principles Applied

1. **Color Scheme**: Modern gradient theme (Purple/Blue gradients)
2. **Typography**: Clean, readable fonts (Inter, Segoe UI)
3. **Spacing**: Generous padding and margins for clarity
4. **Visual Hierarchy**: Clear distinction between sections
5. **Responsive Design**: Mobile-first approach with breakpoints
6. **Accessibility**: High contrast, clear labels, intuitive navigation

---

## 6. Architecture Design

### 6.1 System Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│                    SYSTEM ARCHITECTURE                        │
└──────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────┐
│                    CLIENT TIER                              │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │   Browser   │  │   Browser   │  │   Browser   │      │
│  │ (Student 1) │  │ (Student 2) │  │  (Admin)    │      │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘      │
│         │                 │                 │               │
└─────────┼─────────────────┼─────────────────┼───────────────┘
          │                 │                 │
          │  HTTP/HTTPS      │  HTTP/HTTPS     │  HTTP/HTTPS
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
┌───────────────────────────▼──────────────────────────────────┐
│                    APPLICATION TIER                         │
│  ┌────────────────────────────────────────────────────┐     │
│  │           Flask Web Server (WSGI)                  │     │
│  │  ┌──────────────┐  ┌──────────────┐              │     │
│  │  │   Routes     │  │  Controllers  │              │     │
│  │  │              │  │               │              │     │
│  │  │ - /          │  │ - Auth Logic  │              │     │
│  │  │ - /login     │  │ - Complaint   │              │     │
│  │  │ - /register  │  │   Management │              │     │
│  │  │ - /dashboard │  │ - File Upload │              │     │
│  │  │ - /feedback  │  │ - Validation  │              │     │
│  │  └──────────────┘  └──────────────┘              │     │
│  │                                                    │     │
│  │  ┌────────────────────────────────────┐           │     │
│  │  │   Business Logic Layer             │           │     │
│  │  │   - Authentication                 │           │     │
│  │  │   - Authorization                  │           │     │
│  │  │   - Session Management             │           │     │
│  │  │   - Data Validation                │           │     │
│  │  └────────────────────────────────────┘           │     │
│  └────────────────────────────────────────────────────┘     │
│                            │                                  │
│                            ▼                                  │
│  ┌────────────────────────────────────────────────────┐     │
│  │           Template Engine (Jinja2)                 │     │
│  │  - base.html                                        │     │
│  │  - login.html                                       │     │
│  │  - student_dashboard.html                           │     │
│  │  - admin_dashboard.html                             │     │
│  │  - feedback.html                                     │     │
│  └────────────────────────────────────────────────────┘     │
└───────────────────────────┬───────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                       DATA TIER                              │
│  ┌──────────────────────┐  ┌──────────────────────────┐   │
│  │   SQLite Database    │  │    File System            │   │
│  │                      │  │                          │   │
│  │  ┌────────────────┐  │  │  /static/uploads/       │   │
│  │  │ User Table      │  │  │  - Image Files          │   │
│  │  │ Complaint Table │  │  │    (JPG, PNG, GIF)     │   │
│  │  │ Feedback Table  │  │  │                          │   │
│  │  └────────────────┘  │  │                          │   │
│  └──────────────────────┘  └──────────────────────────┘   │
│            │                                                  │
│            │                                                  │
│  ┌─────────▼──────────────────────────────┐                │
│  │      SQLAlchemy ORM                      │                │
│  │  - Database Abstraction                  │                │
│  │  - Object-Relational Mapping             │                │
│  │  - Query Optimization                    │                │
│  └──────────────────────────────────────────┘                │
└──────────────────────────────────────────────────────────────┘
```

### 6.2 Architecture Pattern: 3-Tier Architecture

#### **Tier 1: Presentation Layer (Client Tier)**
- **Technology**: HTML5, CSS3, JavaScript
- **Responsibilities**:
  - User interface rendering
  - User input collection
  - Client-side validation
  - AJAX requests
- **Components**:
  - Static files (CSS, JS, images)
  - Jinja2 templates
  - Browser-based frontend

#### **Tier 2: Application Layer (Business Logic Tier)**
- **Technology**: Python Flask Framework
- **Responsibilities**:
  - Request routing
  - Authentication and authorization
  - Business logic execution
  - Session management
  - Data validation
- **Components**:
  - Flask application (`app.py`)
  - Route handlers
  - Decorators (login_required, admin_required)
  - File upload handlers

#### **Tier 3: Data Layer (Database Tier)**
- **Technology**: SQLite Database, File System
- **Responsibilities**:
  - Data persistence
  - Data retrieval
  - File storage
  - Transaction management
- **Components**:
  - SQLite database (`hostel_complaints.db`)
  - SQLAlchemy ORM
  - File upload directory
  - Database models (`models.py`)

### 6.3 Technology Stack

#### **Backend:**
- **Framework**: Flask 2.3.3
- **Language**: Python 3.x
- **ORM**: SQLAlchemy (via Flask-SQLAlchemy)
- **Security**: Werkzeug (password hashing)
- **Server**: Flask Development Server (WSGI compatible)

#### **Frontend:**
- **Markup**: HTML5
- **Styling**: CSS3 (with modern features: Flexbox, Grid, Backdrop-filter)
- **Scripting**: Vanilla JavaScript (ES6+)
- **Templating**: Jinja2

#### **Database:**
- **DBMS**: SQLite
- **ORM**: Flask-SQLAlchemy 3.0.5

#### **File Storage:**
- Local file system (`static/uploads/`)
- File type validation (images only)
- File size limit (16MB)

### 6.4 Request-Response Flow

```
1. User Action (Click, Form Submit)
        │
        ▼
2. Browser sends HTTP Request
        │
        ▼
3. Flask Route receives request
        │
        ▼
4. Middleware checks (authentication, authorization)
        │
        ▼
5. Controller processes request
        │
        ▼
6. Business Logic executes
        │
        ▼
7. Database/File System operations
        │
        ▼
8. Data returned to Controller
        │
        ▼
9. Template rendered with data
        │
        ▼
10. HTML Response sent to browser
        │
        ▼
11. Browser renders page
```

### 6.5 Security Architecture

#### **Authentication:**
- Session-based authentication
- Password hashing using Werkzeug's `generate_password_hash`
- Secure password verification using `check_password_hash`
- Session timeout management

#### **Authorization:**
- Role-based access control (RBAC)
- Decorator pattern for route protection
- Admin-specific routes with `admin_required` decorator

#### **Data Protection:**
- SQL injection prevention via SQLAlchemy ORM
- XSS prevention through Jinja2 template escaping
- File upload validation (type and size)
- Secure filename handling

### 6.6 Deployment Architecture

**Development Environment:**
- Flask development server
- SQLite database
- Local file storage
- Debug mode enabled

**Production Considerations:**
- WSGI server (Gunicorn, uWSGI)
- PostgreSQL/MySQL database
- Cloud storage (AWS S3, etc.)
- HTTPS/SSL certificates
- Environment variable configuration
- Production-ready secret keys

### 6.7 Component Interaction Diagram

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│   Browser    │      │ Flask Routes │      │   Database   │
│              │      │              │      │              │
│  HTML/CSS/JS │◄────►│  app.py      │◄────►│ SQLite + ORM │
└──────────────┘      │              │      └──────────────┘
                      │ Templates    │
                      │ Models       │      ┌──────────────┐
                      │              │      │ File System  │
                      └──────────────┘      │  (Uploads)   │
                                            └──────────────┘
```

---

## 7. Conclusion

This project proposal outlines a comprehensive, scalable solution for managing hostel facility complaints in an educational institution. The system addresses real-world problems faced by students and administrators while providing a modern, user-friendly interface.

The architecture is designed for:
- **Maintainability**: Clean code structure, well-documented
- **Scalability**: Can be extended with additional features
- **Reliability**: Robust error handling and validation
- **Security**: Multiple layers of protection
- **Performance**: Efficient database queries and file handling

The proposed system follows industry best practices and provides a solid foundation for a production-ready application with minimal modifications.

---

## Appendix: Key Features Summary

✅ User registration and authentication  
✅ Complaint submission with image upload  
✅ Complaint status tracking   
✅ Admin dashboard with filtering   
✅ Status management workflow   
✅ Feedback system with ratings   
✅ Responsive design   
✅ Session-based security   

**Total Core Functionalities: 7 (Exceeds requirement of 4/5)**

---

*Document Version: 1.0*  
*Last Updated: 2024*  
*Prepared for: Academic Web Development Project*

