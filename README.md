# Book Collection Tracker

A simple Flask web application to manage your personal book collection. Users can register, log in, add, update, delete, and view books. Each user's books are stored separately, ensuring privacy and personalized management. The app features a modern UI, flash messages for feedback, and a search bar for easy navigation.

## Features
- User registration and login
- Add, update, delete, and view books
- Per-user book storage (books are only visible to the logged-in user)
- Flash messages for success/error feedback
- Responsive and modern UI
- Search bar to filter books
- Deployment-ready for Render and GitHub

## Getting Started

### Prerequisites
- Python 3.11+
- pip
- (Optional) Virtual environment

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/chintadavasudharini/Book_Collection_Tracker.git
   cd Book_Collection_Tracker
   ```
2. Create and activate a virtual environment (recommended):
   ```sh
   python -m venv bc
   bc\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Running Locally
1. Start the Flask app:
   ```sh
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`

### Deployment
- The app is ready for deployment on Render or similar platforms.
- Includes `requirements.txt` and `Procfile` for easy setup.

## Project Structure
```
app.py
bc/           # Virtual environment (optional)
static/       # CSS and images
  logstyle.css
  regstyle.css
  wel.css
  image.png
templates/    # HTML templates
  registration.html
  login.html
  dashboard.html
  add.html
  update.html
  view_books.html
  welcome.html
requirements.txt
Procfile
```

## Usage
- Register a new account.
- Log in to your dashboard.
- Add books with title, author, genre, and price.
- Edit or delete your books.
- Use the search bar to quickly find books.
- Log out securely.

## License
This project is licensed under the MIT License.

## Author
Created by chintadavasudharini.
