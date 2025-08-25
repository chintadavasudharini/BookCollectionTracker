📚 Book Collection Tracker

Book Collection Tracker is a Flask-based web application that helps users manage their personal book collections with secure authentication, modern UI, and deployment-ready configurations. It’s designed to provide a smooth, user-friendly experience while ensuring data privacy and scalability.


🚀 Features

🔐 Secure User Authentication – Register and log in with per-user data isolation

📖 Complete Book Management – Add, update, delete, and view books in your collection

🔍 Quick Search – Filter and find books instantly with the integrated search bar

🎨 Responsive Design – Modern, clean, and mobile-friendly interface

⚡ Deployment Ready – Includes requirements.txt and Procfile for hosting on Render, Heroku, or other platforms


🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Database: SQLite (default) – can be extended to PostgreSQL or MySQL

Deployment: Render, GitHub


📂 Project Structure
BookCollectionTracker/
│
├── app.py               # Main Flask app
├── static/              # CSS and image files
│   ├── logstyle.css
│   ├── regstyle.css
│   ├── wel.css
│   └── image.png
├── templates/           # HTML templates
│   ├── welcome.html
│   ├── registration.html
│   ├── login.html
│   ├── dashboard.html
│   ├── add.html
│   ├── update.html
│   └── view_books.html
├── requirements.txt     # Project dependencies
└── Procfile             # For deployment configuration


⚙️ Installation & Setup
Prerequisites

Python 3.11+

pip package manager

(Optional) Virtual environment

Steps

Clone the repository

git clone https://github.com/chintadavasudharini/BookCollectionTracker.git
cd BookCollectionTracker


Create and activate a virtual environment (optional)

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Run the application

python app.py


Open the browser

http://localhost:5000


🌐 Deployment

The app is production-ready and can be easily deployed on Render or similar platforms.

Push the code to a GitHub repository.

Link the repository to your Render account.

The app will deploy automatically using requirements.txt and Procfile.


🎯 Usage

Register for a new account.

Log in to your dashboard.

Add books by entering their title, author, genre, and price.

Edit or delete your books anytime.

Use the search bar to quickly find books in your collection.

Log out securely when done.


📝 License

This project is licensed under the MIT License – free to use and modify.


👩‍💻 Author

Created with ❤️ by chintadavasudharini

Live Demo: [book-collection-tracker.onrender.com](https://book-collection-tracker.onrender.com/)
