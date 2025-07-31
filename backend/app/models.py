# app/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()  # ✅ make sure you only create one instance

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    cost = db.Column(db.Float)
    category = db.Column(db.String)
    name = db.Column(db.String)
    brand = db.Column(db.String)
    retail_price = db.Column(db.Float)
    department = db.Column(db.String)
    sku = db.Column(db.String)
    distribution_center_id = db.Column(db.Integer)

    def to_dict(self):
        return {
            'id': self.id,
            'cost': self.cost,
            'category': self.category,
            'name': self.name,
            'brand': self.brand,
            'retail_price': self.retail_price,
            'department': self.department,
            'sku': self.sku,
            'distribution_center_id': self.distribution_center_id
        }
