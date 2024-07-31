#Question:40.Explain how to set up a Flask application to handle form submissions using POST requests.
#pip install flask
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Q40.html')
    

@app.route('/submit', methods=['POST'])
def submit():
    # Get form data
    name = request.form['name']
    email = request.form['email']
    return f'Hello, {name}! Your email is {email}.'

if __name__ == '__main__':
    app.run(debug=True)
