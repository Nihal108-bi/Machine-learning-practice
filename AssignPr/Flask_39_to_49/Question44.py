#Question 44.How would you create a RESTful API endpoint in Flask that returns JSON data? 
from flask import Flask,jsonify

app=Flask(__name__)

#Sample data to return as JSON
data = {
    "users": [
        {"id": 1, "name": "Nihal", "email": "nihal@example.com"},
        {"id": 2, "name": "nidhi", "email": "nidhi@example.com"}
    ]
}

@app.route('/api/users',methods=['GET'])
def get_users():
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)