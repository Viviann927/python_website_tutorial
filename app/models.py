from app import db, app

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))

    def __repr__(self):
        return '<User %r>' % self.username

@app.before_first_request
def create_tables():
    db.create_all()