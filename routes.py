from app import app,db
from flask import  render_template, url_for, request, redirect
from models import Articles


@app.route('/')
@app.route('/home')
def index():
    return render_template('/index.html')


@app.route('/about')
def about():
    return render_template('/about.html')


@app.route('/posts')
def posts():
    articles = Articles.query.order_by(Articles.date.desc()).all()#desc- от нового к старому
    return render_template('/posts.html', articles=articles)


@app.route('/posts/<int:id>/del')
def post_delete(id):
    article = Articles.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()
        return redirect('/posts')
    except:
        return 'При удалени статьи произошла ошибка '


@app.route('/posts/<int:id>')
def post_detail(id):
    article = Articles.query.get(id)
    return render_template('/post_detail.html', article=article)


@app.route('/posts/<int:id>/update', methods = ['POST', 'GET'])
def post_update(id):
    article = Articles.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.intro = request.form['intro']
        article.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При редактировании страницы произошла ошибка'
    else:
        return render_template('post-update.html', article=article)


@app.route('/create-article', methods = ['POST', 'GET'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']

        article = Articles(title=title, intro = intro, text=text)

        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/posts')
        except:
            return 'При добавлении страницы произошла ошибка'


    else:
        return render_template('create-article.html')