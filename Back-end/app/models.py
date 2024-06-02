from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    is_teacher = db.Column(db.Boolean, default=False)
    is_learner = db.Column(db.Boolean, default=True)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_teacher': self.is_teacher,
            'is_learner': self.is_learner
        }