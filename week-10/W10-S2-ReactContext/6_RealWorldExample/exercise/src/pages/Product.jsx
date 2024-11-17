import React from 'react';
import { useParams } from 'react-router-dom';
import { useBasket } from '../contexts/BasketContext';

import { products } from '../data';

function Product() {
    // TODO: what does this function do?
  const { id } = useParams();
  const product = products.find((p) => p.id === parseInt(id));
  const { addToBasket } = useBasket();

  if (!product) return <p>Product not found</p>;

  return (
    <div className="product-card">
      <h2>{product.name}</h2>
      <p>Price: £{product.price}</p>
      <button onClick={() => addToBasket(product)}>Add to Basket</button>
    </div>
  );
}

export default Product;
