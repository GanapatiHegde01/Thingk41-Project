from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    products = db.relationship('Product', back_populates='department')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    brand = db.Column(db.String(100))
    category = db.Column(db.String(100))
    mrp = db.Column(db.Float)
    retail_price = db.Column(db.Float)
    
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)
    department = db.relationship('Department', back_populates='products')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'mrp': self.mrp,
            'retail_price': self.retail_price,
            'department': {
                'id': self.department.id,
                'name': self.department.name
            }
        }
