from api.core import Mixin
from .base import db


class Film(Mixin, db.Model):
    """Film Table."""

    __tablename__ = "films"

    did = db.Column(db.Integer, unique=True, primary_key=True)
    title = db.Column(db.String, nullable=False)

    def __init__(self, title: str):
        self.title = title

    def __repr__(self):
        return f"<Film {self.title}>"
