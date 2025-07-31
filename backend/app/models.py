from app import db

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    category = db.Column(db.String(100))
    name = db.Column(db.Text)
    brand = db.Column(db.String(100))
    retail_price = db.Column(db.Numeric(10, 2))
    department = db.Column(db.String(100))
    sku = db.Column(db.String(255), unique=True)
    distribution_center_id = db.Column(db.Integer)
