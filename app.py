import os
import base64
import requests
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["IMGBB_API_KEY"] = os.getenv("IMGBB_API_KEY")

mongo = PyMongo(app)

# --- Routes ---

@app.route('/')
def index():
    # Fetch all projects from MongoDB
    projects = mongo.db.projects.find()
    return render_template('index.html', projects=projects)

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == os.getenv('ADMIN_USER') and password == os.getenv('ADMIN_PASS'):
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash("Invalid Credentials", "danger")
            
    return render_template('login.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form.get('title')
        link = request.form.get('link')
        image_file = request.files.get('image')
        
        if image_file:
            # Upload to ImgBB
            base64_image = base64.b64encode(image_file.read())
            payload = {
                "key": app.config["IMGBB_API_KEY"],
                "image": base64_image
            }
            res = requests.post("https://api.imgbb.com/1/upload", data=payload)
            
            if res.status_code == 200:
                image_url = res.json()['data']['url']
                mongo.db.projects.insert_one({
                    'title': title,
                    'image': image_url,
                    'link': link
                })
                flash("Project added successfully!", "success")
                return redirect(url_for('admin'))
    
    projects = mongo.db.projects.find()
    return render_template('admin.html', projects=projects)

@app.route('/delete/<project_id>')
def delete_project(project_id):
    if session.get('admin_logged_in'):
        mongo.db.projects.delete_one({'_id': ObjectId(project_id)})
    return redirect(url_for('admin'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)