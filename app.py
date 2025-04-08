from flask import Flask,render_template, request,redirect,url_for,flash
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
app.secret_key="securekey" # Needed for flash messages
UPLOAD_FOLDER='uploads'
ALLOWED_EXTENSIONS={'png','jpg','jpeg','pdf'}
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def index():
    return render_template('index.html') # Your HTML file should be saved in templates/index.html
@app.route('/submit', methods=['POST'])
def submit():
    name=request.form.get('name')
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')
    file=request.files.get('file')

    print(f"Name: {name}, Email: {email}, Phone: {phone}, Message: {message}")

    if file and allowed_file(file.filename):
        filename=secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(f"File saved: {filename}")
    else:
        print("No file uploaded or file type not allowed.")

    flash('Form submitted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)