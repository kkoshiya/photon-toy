from flask import (Flask, render_template)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/blog')
def blog():
  return render_template('blog.html')
