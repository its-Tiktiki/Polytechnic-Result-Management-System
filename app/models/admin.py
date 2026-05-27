from app.extensions import db

class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50),nullable=False,unique=True)
    password = db.Column(db.String(120), nullable=False)