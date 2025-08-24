from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

user_books = {}  # key: username, value: list of books
users = []  # List to store user data

@app.route('/')
def home():
    return render_template('welcome.html', books=[])

@app.route('/registration', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Add your registration logic here (e.g., save to database, validate input, etc.)
        if password == confirm_password:
            users.append({'username': username, 'email': email, 'password': password})
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Passwords do not match!', 'danger')

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        if user:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html')

# Dashboard page route
@app.route('/dashboard')
def dashboard():
    username = session.get('username')
    user = next((u for u in users if u['username'] == username), None) if username else None
    books = user_books.get(username, []) if username else []
    return render_template('dashboard.html', books=books, user=user)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    username = session.get('username')
    if not username:
        flash('You must be logged in to add books.', 'danger')
        return redirect(url_for('login'))
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        books = user_books.setdefault(username, [])
        book_id = len(books) + 1
        books.append({'id': book_id, 'title': title, 'author': author, 'genre': genre, 'price': price})
        flash('Books added successfully!', 'success')
        return redirect(url_for('view_books'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    username = session.get('username')
    if not username:
        flash('You must be logged in to update books.', 'danger')
        return redirect(url_for('login'))
    books = user_books.get(username, [])
    book = next((b for b in books if b['id'] == id), None)
    if not book:
        flash('Book not found.', 'danger')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['genre'] = request.form['genre']
        book['price'] = request.form['price']
        flash('Book updated successfully!', 'success')
        return redirect(url_for('view_books'))
    return render_template('update.html', book=book)
# View all books route
@app.route('/view_books')
def view_books():
    username = session.get('username')
    books = user_books.get(username, []) if username else []
    return render_template('view_books.html', books=books)

@app.route('/delete/<int:id>')
def delete_book(id):
    username = session.get('username')
    if not username:
        flash('You must be logged in to delete books.', 'danger')
        return redirect(url_for('login'))
    books = user_books.get(username, [])
    user_books[username] = [b for b in books if b['id'] != id]
    flash('Book deleted successfully!', 'success')
    return redirect(url_for('view_books'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)