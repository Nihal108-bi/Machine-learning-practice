#Question 41.Write a Flask route that accepts a parameter in the URL and displays it on the page.
#pip install flask

from flask import Flask,render_template_string
app=Flask(__name__)
@app.route('/display/<name>')
def display_name(name):
    return render_template_string('<h1>Hello,{{name}}!</h1>',name=name)

if __name__=='__main__':
    app.run(debug=True)








    #http://127.0.0.1:5000/display/YourName          #use this url for seeing your name