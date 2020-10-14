from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #primary_key говорит что значение id должно бть уникальным
    title = db.Column(db.String(100), nullable = False)
    intro = db.Column(db.String(300), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __rapr__(self):
        return '<Article {}>'.format(self.id)

@app.route('/')
@app.route('/home')
def index():
    return render_template('/index.html')


@app.route('/about')
def about():
    return render_template('/about.html')


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
            return redirect('/')
        except:
            return 'При добавлении страницы произошла ошибка'


    else:
        return render_template('create-article.html')

if __name__ == '__main__':
    app.run(debug=True)