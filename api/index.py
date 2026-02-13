from flask import Flask, redirect, url_for, render_template
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = os.environ.get('SECRET_KEY', 'your-love-secret-key-2026')

@app.route('/')
def home():
    return render_template("lamp.html")

@app.route('/user')
def user(): 
    return render_template("Love.html")

@app.route('/love2')
def love2(): 
    return render_template("love2.html")

@app.route('/chocolate')
def chocolate2():
    return render_template("chocolate2.html")

@app.route('/love3')
def love3(): 
    return render_template("love3.html")

@app.route('/love4')
def love4(): 
    return render_template("love4.html")

@app.route('/pic')
def pic():
    return render_template("pic.html")
