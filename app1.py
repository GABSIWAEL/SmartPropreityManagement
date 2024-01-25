from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'drhcfgjh34567GHJCNVNBN'

# Configure MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'smart property'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def index():
    # Check for the 'logout' query parameter
    logout_param = request.args.get('logout')

    if logout_param:
        # If 'logout' parameter is present, add a JavaScript code to prevent going back
        return render_template('login.html', logout=True)
    else:
        return render_template('login.html')


@app.route('/account_settings', methods=['GET', 'POST'])
def account_settings():
    username = session.get('username')

    if request.method == 'POST':
        new_username = request.form.get('new_username')
        new_password = request.form.get('new_password')

        cur = mysql.connection.cursor()

        # Update the username and password in the MySQL database
        if new_username:
            cur.execute(
                "UPDATE users SET username = %s WHERE username = %s", (new_username, username))
            session['username'] = new_username

        if new_password:
            cur.execute(
                "UPDATE users SET password = %s WHERE username = %s", (new_password, username))

        mysql.connection.commit()
        cur.close()

    # Fetch all users from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()

    return render_template('account_settings.html', username=username, users=users)


@app.route('/homepage')
def homepage():
    # Retrieve the username from the session
    username = session.get('username')

    # Check if the user is authenticated
    if username:
        return render_template('index.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    cur = mysql.connection.cursor()

    # Check if the entered credentials are valid
    cur.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cur.fetchone()
    cur.close()

    if user:
        # Authentication successful, store username in the session
        session['username'] = username
        # Redirect to the homepage
        return redirect(url_for('homepage'))
    else:
        # Authentication failed, redirect to the login page with query parameters
        return redirect(url_for('index', error='Invalid credentials'))


@app.route('/update_user', methods=['POST'])
def update_user():
    data = request.get_json()
    old_username = data.get('oldUsername')
    new_username = data.get('newUsername')

    cur = mysql.connection.cursor()

    try:
        cur.execute(
            "UPDATE users SET username = %s WHERE username = %s", (new_username, old_username))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': f'User {old_username} updated to {new_username} successfully.'})
    except Exception as e:
        return jsonify({'message': f'Error updating user: {str(e)}'})


@app.route('/remove_user', methods=['POST'])
def remove_user():
    data = request.get_json()
    username = data.get('username')

    cur = mysql.connection.cursor()

    try:
        cur.execute("DELETE FROM users WHERE username = %s", (username,))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': f'User {username} removed successfully.'})
    except Exception as e:
        return jsonify({'message': f'Error removing user: {str(e)}'})


@app.route('/home')
def home():
    # Similar modifications as in the homepage route
    username = session.get('username')
    if username:
        return render_template('home.html', username=username)
    else:
        return redirect(url_for('index'))


# ... (Similar modifications for other routes)

@app.route('/garden')
def garden():
    # Similar modifications for other routes
    username = session.get('username')
    if username:
        return render_template('garden.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/farm')
def farm():
    username = session.get('username')
    if username:
        return render_template('farm.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/farmHouse')
def farmHouse():
    username = session.get('username')
    if username:
        return render_template('farmHouse.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/restaurantHammamet')
def restaurantHammamet():
    username = session.get('username')
    if username:
        return render_template('RestaurantHammamet.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/coffeHammamet')
def coffeHammamet():
    username = session.get('username')
    if username:
        return render_template('CoffeHammamet.html', username=username)
    else:
        return redirect(url_for('index'))


@app.route('/logout')
def logout():
    # Clear the session when the user logs out
    session.pop('username', None)

    # Redirect to the index page with a unique query parameter
    return redirect(url_for('index', logout=True))


if __name__ == '__main__':
    app.run(debug=True)
