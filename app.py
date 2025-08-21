from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

books = []
users = []  # List to store user data

@app.route('/')
def home():
    return render_template('welcome.html', books=books)

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
    return render_template('dashboard.html', books=books, user=user)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        price = request.form['price']
        books.append({'id': len(books) + 1, 'title': title, 'author': author, 'genre': genre, 'price': price})
        return redirect(url_for('dashboard'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = next((b for b in books if b['id'] == id), None)
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        book['genre'] = request.form['genre']
        book['price'] = request.form['price']
        return redirect(url_for('dashboard'))
    return render_template('update.html', book=book)
# View all books route
@app.route('/view_books')
def view_books():
    return render_template('view_books.html', books=books)

@app.route('/delete/<int:id>')
def delete_book(id):
    global books
    books = [b for b in books if b['id'] != id]
    return redirect(url_for('dashboard'))
@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)