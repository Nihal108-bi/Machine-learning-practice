#Q43.Describe the process of connecting a Flask app to a SQLite database using SQLAlchemy.

#pip install Flask SQLAlchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Initialize flask application
app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

#intialise SQLAlchemy
db=SQLAlchemy(app)

#define a model
class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)

    def __repr__(self):
        return f"<User {self.username}>"
    
#create the database and the tables

with app.app_context():
    db.create_all()   

#Define a simple route

@app.route('/')
def home():
    return "Hello,Nihal!"

#Run the flask application
if __name__=='__main__':
    app.run(debug=True)     