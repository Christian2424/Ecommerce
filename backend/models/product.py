from database import db
from models.collection import Collection

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    img_url = db.Column(db.String(255), nullable=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
