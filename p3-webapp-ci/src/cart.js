/**
 * QuickCart checkout helpers (Lab 3).
 *
 * SPEC: all money values returned by this module must be rounded to
 * exactly 2 decimal places.
 */

function subtotal(items) {
  return items.reduce((sum, it) => sum + it.price * it.qty, 0);
}

/**
 * Applies a percentage discount to a cart.
 * @param {Array<{name: string, price: number, qty: number}>} items
 * @param {number} discountPercent  e.g. 10 means -10%
 * @returns {number} final total, rounded to 2 decimals per the spec
 */
function applyDiscount(items, discountPercent) {
  const raw = subtotal(items) * (1 - discountPercent / 100);
  return Math.round(raw * 100) / 100; // <-- BUG: rounds to ONE decimal place
}

module.exports = { subtotal, applyDiscount };
