from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
cors = CORS(app, origins='*')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app);

class SaleSystem(db.Model): 
    id=db.Column(db.Integer,primary_key=True)
    menu_item=db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Float, default=0)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

@app.route('/place_order', method=['POST'])
def place_order():
    data = request.get_json()
    menu_item = data.get('menu_item')
    cost = data.get('cost')

    if not menu_item or not cost:
        return jsonify({'error': 'Menu item and cost are required.'}), 400
    
    new_order = SaleSystem(menu_item=menu_item, cost=cost)
    db.session.add(new_order)
    db.session.commit()

    return jsonify({'message': 'Order placed successfully.', 'order_id': new_order.id})





#with app.app_context(): #USED TO CREATE 'test.db' FILE
   #db.create_all()

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/') #root URL
def index():
    return render_template('index.html')

@app.route('/aboutme') #about me URL
def aboutme():
    return render_template('aboutme.html')

@app.route('/order') #order page URL
def order():
    return render_template('order.html') 

@app.route('/shop') #shop page w/ menu
def shop():
    return render_template('shop.html')

if __name__ == "__main__":
    app.run(debug=True)
