from flask import render_template, request, redirect
from cloudipsp import Api, Checkout

from utils.db_utils import db_create, db_exist
from models.data import db, Item
from app import create_app


app = create_app()

@app.route('/')
def index():

    db_create() # Create DB if not exist
    db.create_all() # Create tables if not exist

    items = Item.query.order_by(Item.price).all()    
    return render_template('index.html', items=items)

@app.route('/buy/<int:id>')
def item_buy(id):

    item = Item.query.get(id)

    api = Api(merchant_id=1396424,
            secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": int(item.price * 100)
    }
    
    url = checkout.url(data).get('checkout_url')

    return redirect(url)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/create', methods=['GET', 'POST']) 
def create():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        item = Item(name=name, price=price, description=description)

        try:
            db.session.add(item)
            db.session.commit()
            return redirect('/')
        except Exception as error:
            return f'Error: {error}'
    else:
        return render_template('create.html')
