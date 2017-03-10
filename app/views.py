from flask import render_template, request, redirect, url_for

from app import app, babel
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


@app.route('/edit', methods=['POST'])
def edit():
    quote_id = request.form['quote_id']
    content = request.form['content']
    next_ = request.form['next']

    quote = Quote.get(id=quote_id)
    quote.content = content
    quote.save()

    return redirect(next_)


@app.route('/<int:quote_id>')
def quote(quote_id):
    quote = Quote.get(id=quote_id)
    return render_template('quote.html', quote=quote)


@babel.localeselector
def get_locale():
    return app.config['LOCALE']
