from app import create_app, db
from app.load_data import load_products_from_csv

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        load_products_from_csv('products.csv')
