from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
from models import collection, product, user, cartitem, order, orderitem
from models.collection import Collection
from models.product import Product
from models.orderitem import OrderItem
from sqlalchemy import func
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce_home.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route("/getcollection")
def get_collection():
    all_collection = Collection.query.all()
    return jsonify(all_collection)


@app.route("/getbestseller")
def get_products():

    bestsellers = db.session.query(Product)\
        .join(OrderItem, Product.id == OrderItem.product_id)\
        .group_by(Product.id)\
        .order_by(func.sum(OrderItem.quantity).desc())\
        .limit(4)\
        .all()

    list_bestseller = []
    for product in bestsellers:
        list_bestseller.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'img_url': product.img_url,
        })

    return jsonify(list_bestseller)

if __name__ == '__main__':
    app.run(debug=True)