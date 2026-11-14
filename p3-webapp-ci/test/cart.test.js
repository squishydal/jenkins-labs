const { applyDiscount } = require("../src/cart");

describe("checkout totals", () => {
  const cart = [
    { name: "Coffee beans 1kg", price: 19.99, qty: 2 },
    { name: "Filter papers", price: 3.49, qty: 1 },
    { name: "Mug", price: 12.5, qty: 1 },
  ];

  test("no discount returns the exact subtotal", () => {
    expect(applyDiscount(cart, 0)).toBeCloseTo(55.97, 2);
  });

  test("10% discount is rounded to 2 decimals", () => {
    // 55.97 * 0.9 = 50.373  ->  the spec says 50.37
    expect(applyDiscount(cart, 10)).toBeCloseTo(50.37, 2);
  });

  test("25% discount is rounded to 2 decimals", () => {
    // 55.97 * 0.75 = 41.9775  ->  the spec says 41.98
    expect(applyDiscount(cart, 25)).toBeCloseTo(41.98, 2);
  });

  test("100% discount empties the cart", () => {
    expect(applyDiscount(cart, 100)).toBe(0);
  });
});
