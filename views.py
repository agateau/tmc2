from flask import render_template, request, redirect

from app import app
from models import Quote


@app.route('/', methods=['GET'])
def homepage():
    quotes = Quote.public().limit(50)
    return render_template('homepage.html', quotes=quotes)


@app.route('/add', methods=['POST'])
def add():
    if request.form.get('content'):
        Quote.create(content=request.form['content'])
    return redirect('/')
