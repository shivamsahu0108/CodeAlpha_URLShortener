# CodeAlpha URL Shortener

A simple URL Shortener backend developed as part of the **CodeAlpha Backend Development Internship**.

The application accepts a long URL, generates a unique short code, stores the URL mapping in a SQLite database, and redirects users from the short URL to the original URL.

## 🚀 Features

- Create a short URL from a long URL
- Generate unique short codes
- Store URL mappings in SQLite
- Redirect short URLs to the original URLs
- Validate required URL input
- Return appropriate HTTP status codes
- REST API-based backend

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLite**
- **Postman** for API testing

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

> `venv/` and the local database file are excluded from Git using `.gitignore`.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shivamsahu0108/CodeAlpha_URLShortener.git
```

### 2. Open the project

```bash
cd CodeAlpha_URLShortener
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Windows CMD

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask server:

```bash
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

## 🔌 API Endpoints

### 1. Check API Status

**GET**

```text
/
```

Example:

```text
http://127.0.0.1:5000/
```

Response:

```text
URL Shortener API is running!
```

---

### 2. Create Short URL

**POST**

```text
/api/urls
```

Request body:

```json
{
  "url": "https://www.google.com"
}
```

Example response:

```json
{
  "message": "URL shortened successfully",
  "originalUrl": "https://www.google.com",
  "shortCode": "aB72xQ",
  "shortUrl": "http://127.0.0.1:5000/aB72xQ"
}
```

### 3. Redirect to Original URL

**GET**

```text
/<short_code>
```

Example:

```text
http://127.0.0.1:5000/aB72xQ
```

The application looks up the short code in the database and redirects the user to the stored original URL.

## 🗄️ Database

The application uses **SQLite** with **Flask-SQLAlchemy**.

The URL table contains:

| Column         | Description                 |
| -------------- | --------------------------- |
| `id`           | Unique database ID          |
| `original_url` | Original long URL           |
| `short_code`   | Generated unique short code |

## 🧪 Testing

The following functionality has been tested successfully:

- Flask server startup
- API status endpoint
- URL shortening
- Unique short-code generation
- Database storage
- Short URL redirection
- Missing URL validation
- Invalid short-code handling
- Multiple URL creation
- Database persistence

The APIs were tested using **Postman**.

## 📌 CodeAlpha Internship

This project was developed as part of the **CodeAlpha Backend Development Internship — Task 1: Simple URL Shortener**.

## 👨‍💻 Author

**Shivam Sahu**

GitHub:  
`https://github.com/shivamsahu0108`

LinkedIn:  
`https://www.linkedin.com/in/shivam-sahu-bb506b345/`
