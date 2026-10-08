from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random

app = Flask(__name__)

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///urls.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# URL Model
class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_code = db.Column(db.String(10), unique=True, nullable=False)


# Generate unique short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = "".join(random.choices(characters, k=length))

        existing_url = URL.query.filter_by(short_code=code).first()

        if not existing_url:
            return code


# Home
@app.route("/")
def home():
    return "URL Shortener API is running!"


# Create short URL
@app.route("/api/urls", methods=["POST"])
def create_short_url():

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({
            "error": "URL is required"
        }), 400

    original_url = data["url"]

    short_code = generate_short_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "message": "URL shortened successfully",
        "originalUrl": original_url,
        "shortCode": short_code,
        "shortUrl": f"http://127.0.0.1:5000/{short_code}"
    }), 201


# Redirect to original URL
@app.route("/<short_code>")
def redirect_to_original(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if not url:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    return redirect(url.original_url)


# Create database
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)