from flask_sqlalchemy import SQLAlchemy
import psycopg2


db = SQLAlchemy()

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return self.name
