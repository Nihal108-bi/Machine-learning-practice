#Q 39.How would you create a basic Flask route that displays "Hello, World!" on the homepage?
#pip install flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello,world!'

if __name__=='__main__':
    app.run(debug=True)