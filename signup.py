from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='template')
app.secret_key = 'hello123'

# Dummy user data (replace with a database in a real-world scenario)
users = {'example_user': 'password123'}

@app.route('/')
def home():
    return 'Welcome to the Home Page'

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username is already taken
        if username in users:
            error = 'Username already taken. Please choose another username.'
            return render_template('signup.html', error=error)

        # Store the user in the "database"
        users[username] = password

        # Log in the user (you may want to customize this part based on your needs)
        session['username'] = username

        return redirect(url_for('dashboard'))

    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f'Welcome to the Dashboard, {username}!'
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
