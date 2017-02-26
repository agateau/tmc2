from flask import render_template, request, redirect, url_for

from app import app
from models import Quote


@app.route('/', methods=['GET'])
def homepage():
    try:
        page = int(request.args.get('page'))
    except TypeError:
        page = 0
    quotes, page_count = Quote.paged(page, app.config['PAGE_SIZE'])

    return render_template('homepage.html', quotes=quotes, page=page,
                           page_count=page_count)


@app.route('/add', methods=['POST'])
def add():
    if request.form.get('content'):
        Quote.create(content=request.form['content'])
    return redirect(url_for('homepage'))
