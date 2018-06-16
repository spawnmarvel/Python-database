from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == "__main__":
    db.create_all()
    
    # add
    # u = User(username="john", email="john@com")
    # p = User(username="tim", email="tim@com")
    # db.session.add(u)
    # db.session.add(p)
    # db.session.commit()
    print(User.query.all())

    
    # delete
    #  rm = User.query.filter_by(email='john@com').first()
    # db.session.delete(rm)
    # db.session.commit()
    
    # get properties
    u = User.query.filter_by(email="john@com").first()
    print(u.email)
    print(User.query.all())
