from app import db

class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(16))
    description = db.Column(db.String(128))
    full_description = db.Column(db.String(1024))

    def __init__(self, title, description, full_description):
        self.title = title
        self.description = description
        self.full_description = full_description
