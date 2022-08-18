from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RegisterModel(db.Model):
    __tablename__ = 'regester_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    intime = db.Column(db.DateTime)
    outtime = db.Column(db.DateTime)
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

def init_db(app):
    db.init_app(app)
    db.create_all()

def get_all():
    return RegisterModel.order_by(RegisterModel.id).all()

def insert(name, intime, outtime, comment):
    model = RegisterModel(name=name, intime=intime, outtime=outtime, comment=comment)
    db.session.add(model)
    db.session.commit()
