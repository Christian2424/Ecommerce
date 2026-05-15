from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from database import db
from models import collection, product, user, cartitem, order, orderitem
from sqlalchemy import func


app = Flask(__name__)
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
    bestseller = db.session.query(
        Product, 
        func.count(OrderItem.id).label('numero_vendite')
    ).join(OrderItem, Product.id == OrderItem.product_id) \
    .group_by(Product.id) \
    .order_by(func.desc('numero_vendite')) \
    .limit(4) \
    .all()

    list_bestseller = []
    for product in bestseller:
        list_bestseller.append({
            'id': product[0].id,
            'name': product[0].name,
            'price': product[0].price,
            'img_url': product[0].img_url,
            'collection_id': product[0].collection_id,
            'numero_vendite': product[1]
        })

    return jsonify(list_bestseller)

if __name__ == '__main__':
    app.run(debug=True)