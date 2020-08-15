from dbs import db
from sqlalchemy.orm import relationship


class student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)



class socre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    python = db.Column(db.Integer, nullable=False)
    java = db.Column(db.Integer, nullable=False)
    english = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    s_student = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    g_student = relationship('student', backref='scoree')

