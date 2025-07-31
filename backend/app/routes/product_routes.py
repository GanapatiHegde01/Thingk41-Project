# app/routes/product_routes.py
from flask import Blueprint, request
from app.models import Product  # ✅ import model only
from app.utils.response import success_response, error_response

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    return success_response([p.to_dict() for p in products])

@product_bp.route('/api/products/<id>', methods=['GET'])
def get_product_by_id(id):
    try:
        product_id = int(id)
    except ValueError:
        return error_response("Invalid product ID format", 400)

    product = Product.query.get(product_id)
    if not product:
        return error_response("Product not found", 404)

    return success_response(product.to_dict())
