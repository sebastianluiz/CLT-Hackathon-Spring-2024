from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app);

class SaleSystem(db.Model): 
    id=db.Column(db.Integer,primary_key=True)
    menu_item=db.Column(db.String(200), nullable=False)
    cost = db.Column(db.Float, default=0)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.now)

#with app.app_context(): #USED TO CREATE 'test.db' FILE
   #db.create_all()

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

    