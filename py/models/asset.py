from app import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(16))
    description = db.Column(db.String(64))

    def __init__(self, title, description):
        self.title = title
        self.description = description