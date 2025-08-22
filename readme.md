# ☕ Cafe Finder App

A Flask-based web application where users can **discover cafes**, **suggest new cafes**, and **manage accounts** with authentication.  
The app supports login, registration, and CRUD operations for cafes with secure password handling.  

---

## 🚀 Features
- 🔐 User Authentication (Register, Login, Logout)
- 👥 Secure password hashing with **Werkzeug**
- ☕ Add and view cafes with details:
  - Name, Location, Map URL, Image URL
  - Availability of sockets, WiFi, toilets, and call-friendly environment
  - Seating info and coffee prices
- 🛡 CSRF Protection enabled
- 🎨 Styled with **Flask-Bootstrap5**
- 🗄 Persistent data storage with **SQLite + SQLAlchemy ORM**

---

## 🛠 Tech Stack
- **Backend:** Flask, Flask-Login, Flask-WTF
- **Frontend:** Flask-Bootstrap5, Jinja2 templates
- **Database:** SQLite + SQLAlchemy ORM
- **Security:** CSRFProtect, Password Hashing (pbkdf2:sha256)

---
