
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging

app = Flask(__name__)

app.secret_key = 'your_secret_key'
users = {'admin': 'admin', 'user2': 'password2'}

# Configure the logging module
logging.basicConfig(filename='error.log', level=logging.ERROR)


# Custom error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Custom error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    # Log the exception details
    logging.exception("An internal server error occurred")

    return render_template('500.html'), 500

@app.errorhandler(Exception)
def handle_exception(error):
    # Log the exception details
    logging.exception("An error occurred")

    response = {'error': 'Internal Server Error', 'message': str(error)}
    return jsonify(response), 500

@app.route('/')
def hello_world():
    str="""
    <html>
    <head>
    <title>Sahil's App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    </head>
    <body style="">
    <h1>Hello From Sahil</h1>
    </body>
    </html>
    """
    return redirect(url_for('login'))

@app.route('/Hello/<name>')
def hello(name):
    return 'Hello to %s!' %name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password match
        if username in users and users[username] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('hello_world'))
        else:
            flash('Invalid username or password', 'error')

    return render_template('login.html')



if __name__=='__main__':
    app.run()