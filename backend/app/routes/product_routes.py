from flask import Blueprint, request
from app.models import Product
from app.utils.response import success_response, error_response

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/api/products', methods=['GET'])
def get_all_products():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
    except ValueError:
        return error_response("Invalid pagination parameters", 400)

    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    products = [p.to_dict() for p in pagination.items]

    return success_response({
        "page": pagination.page,
        "per_page": pagination.per_page,
        "total": pagination.total,
        "pages": pagination.pages,
        "data": products
    })


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
