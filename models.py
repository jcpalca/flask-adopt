"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG_URL = "https://cdn.pixabay.com/photo/2015/06/12/18/44/fox-807315_960_720.png"

def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(50),
                     nullable=False)
    species = db.Column(db.String(30),
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable=False,
                          default=DEFAULT_IMG_URL)
    age = db.Column(db.String(6),
                    nullable=False)
    notes = db.Column(db.Text,
                      nullable=False,
                      default="")
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
