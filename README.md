# CodeAlpha URL Shortener

A simple and efficient URL Shortener backend developed as part of the **CodeAlpha Backend Development Internship**.

The application accepts a long URL, generates a unique short code, stores the URL mapping in a SQLite database, and redirects users from the short URL to the original URL.

---

## 🚀 Features

- Create a short URL from a long URL
- Generate unique short codes
- Store URL mappings in SQLite
- Redirect short URLs to original URLs
- Validate required URL input
- Handle invalid short URLs
- Return appropriate HTTP status codes
- REST API-based backend

---

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **Postman** for API testing

---

## 📁 Project Structure

```text
CodeAlpha_URLShortener/
│
├── instance/
│   └── urls.db
│
├── venv/
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```
