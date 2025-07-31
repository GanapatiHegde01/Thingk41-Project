import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(`http://localhost:5000/api/products/${id}`)
      .then(res => res.json())
      .then(data => {
        if (data.success) setProduct(data.data);
        else setError(data.message);
      })
      .catch(err => setError('Something went wrong'));
  }, [id]);

  if (error) return <p>{error}</p>;
  if (!product) return <p>Loading...</p>;

  return (
    <div className="detail">
      <h2>{product.name}</h2>
      <p><strong>Brand:</strong> {product.brand}</p>
      <p><strong>Category:</strong> {product.category}</p>
      <p><strong>Department:</strong> {product.department}</p>
      <p><strong>SKU:</strong> {product.sku}</p>
      <p><strong>Price:</strong> ₹{product.retail_price}</p>
      <p><strong>Cost:</strong> ₹{product.cost}</p>
      <p><strong>Distribution Center ID:</strong> {product.distribution_center_id}</p>
      <Link to="/" className="back">← Back to Products</Link>
    </div>
  );
}

export default ProductDetail;
