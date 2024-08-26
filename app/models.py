from . import db

class Query(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(256))
    result = db.Column(db.Text)

    def __repr__(self):
        return f'<Query {self.domain}>'
