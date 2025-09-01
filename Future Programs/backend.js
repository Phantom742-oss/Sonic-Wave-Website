const products = [
    { name: "Product 1", image: "product1.jpg", price: "$10" },
    { name: "Product 2", image: "product2.jpg", price: "$20" },
    { name: "Product 3", image: "product3.jpg", price: "$30" }
  ];
  
  const productsList = document.querySelector("#products");
  
  for (const product of products) {
    const productItem = document.createElement("li");
    productItem.innerHTML = `
      <h3>${product.name}</h3>
      <img src="${product.image}" alt="${product.name}">
      <p>${product.price}</p>
    `;
    productsList.appendChild(productItem);
  }
  