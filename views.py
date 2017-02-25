from flask import render_template, request

from app import app
from models import Quote


@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        if request.form.get('content'):
            # Create a new quote in the db.
            Quote.create(content=request.form['content'])

    quotes = Quote.public().limit(50)
    return render_template('homepage.html', quotes=quotes)
