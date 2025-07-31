import pandas as pd
from app.models import Product
from app import db

def load_products_from_csv(csv_path):
    df = pd.read_csv(csv_path)

    for _, row in df.iterrows():
        product = Product(
            id=row['id'],
            cost=row['cost'],
            category=row['category'],
            name=row['name'],
            brand=row['brand'],
            retail_price=row['retail_price'],
            department=row['department'],
            sku=row['sku'],
            distribution_center_id=row['distribution_center_id']
        )
        db.session.add(product)

    db.session.commit()
    print(f"✅ Loaded {len(df)} products into the database.")
