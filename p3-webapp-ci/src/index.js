const { applyDiscount } = require("./cart");

const cart = [
  { name: "Coffee beans 1kg", price: 19.99, qty: 2 },
  { name: "Filter papers", price: 3.49, qty: 1 },
  { name: "Mug", price: 12.5, qty: 1 },
];

console.log("QuickCart demo checkout");
console.log("Items in cart: " + cart.length);
console.log("Total after 10% discount: $" + applyDiscount(cart, 10));
