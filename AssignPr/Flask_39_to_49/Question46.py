#Question 46.How can you implement file uploads in a Flask application??

from flask import Flask,request,redirect,url_for,render_template
import os

#Initialize the flask appliction
app=Flask(__name__)

#Configure the upload folder and allowed extentions

UPLOAD_FOLDER='uploads'
ALLOWED_EXTENSIONS={'txt','pdf','png','jpg','jpeg','gif','py'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

#Ensure the upload foler exists

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

def allowed_file(filename):
    return '.'in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#Route to render theupload form
@app.route('/')
def upload_form():
    return render_template('Q46_upload_form.html')

#Route to handle file upload 
@app.route('/upload',methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file=request.files['file']
    if file.filename=='':
        return 'No selected file'
    
    if file and allowed_file(file.filename):
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return f'File {filename} upload succesfully'
    
    return 'File type not allowed'

if __name__=='__main__':
    app.run(debug=True)