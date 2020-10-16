from datetime import datetime

from app import app




class Articles(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    #primary_key говорит что значение id должно бть уникальным
    title = db.Column(db.String(100), nullable = False)
    intro = db.Column(db.String(300), nullable = False)
    text = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __rapr__(self):
        return '<Article {}>'.format(self.id)

