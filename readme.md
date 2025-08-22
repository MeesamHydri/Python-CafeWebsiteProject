# Cafe and Wifi Finder

A Flask web application to browse cafes, suggest new cafes, and manage users with registration and login functionality. The app uses **Flask**, **Flask-Login**, **Flask-Bootstrap**, **Flask-WTF**, and **SQLite** for the database.

---

## Features

- User registration and login with hashed passwords.
- Secure sessions with Flask-Login.
- Browse a list of cafes with details including:
  - Name, location, map link, image
  - Amenities: Wi-Fi, sockets, toilets, phone-call friendly
  - Seats and coffee prices
- Suggest a new cafe via a form.
- Flash messages for feedback (success, error, info).
- CSRF protection on forms.

---

## Tech Stack

- **Backend:** Flask, Flask-Login, SQLAlchemy
- **Frontend:** Bootstrap 5 (via Flask-Bootstrap)
- **Database:** SQLite
- **Forms:** Flask-WTF with CSRF protection
- **Password Security:** Werkzeug hashing (`pbkdf2:sha256`)

---

## Installation

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd <repo-directory>
