from project import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(100))
    height = db.Column(db.Integer)
    weight = db.Column(db.Float)
    complexion = db.Column(db.String(20))
    age = db.Column(db.Integer)
    bio = db.Column(db.Text)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    

    def __repr__(self):
        return f"<Profile {self.email}>"
