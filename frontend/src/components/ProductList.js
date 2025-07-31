import React, { useEffect, useState } from 'react';
import ProductCard from './ProductCard';

function ProductList() {
  const [products, setProducts] = useState([]);
  const [pageInfo, setPageInfo] = useState({ page: 1, per_page: 10, total: 0, pages: 0 });
  const [loading, setLoading] = useState(true);

  const fetchProducts = async (page = 1) => {
    setLoading(true);
    try {
      const response = await fetch(`http://localhost:5000/api/products?page=${page}&per_page=${pageInfo.per_page}`);
      const result = await response.json();
      if (result.success) {
        setProducts(result.data.data);
        setPageInfo({
          page: result.data.page,
          per_page: result.data.per_page,
          total: result.data.total,
          pages: result.data.pages
        });
      }
    } catch (err) {
      console.error('Fetch error:', err);
    }
    setLoading(false);
  };

  useEffect(() => {
    fetchProducts(pageInfo.page);
    // eslint-disable-next-line
  }, []);

  const handlePageChange = (newPage) => {
    if (newPage >= 1 && newPage <= pageInfo.pages) {
      fetchProducts(newPage);
    }
  };

  return (
    <div>
      <h2 className="title">Product List</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <div className="grid">
            {products.map(product => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>

          <div className="pagination">
            <button onClick={() => handlePageChange(pageInfo.page - 1)} disabled={pageInfo.page === 1}>
              ⬅ Previous
            </button>
            <span>
              Page {pageInfo.page} of {pageInfo.pages}
            </span>
            <button onClick={() => handlePageChange(pageInfo.page + 1)} disabled={pageInfo.page === pageInfo.pages}>
              Next ➡
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default ProductList;
