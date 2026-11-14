package com.jenkinslab.invoice;

import java.util.List;

/**
 * Tiny invoice calculator for the Jenkins Maven lab.
 * Quantity discounts: 10+ units of one line item = 5% off, 50+ = 10% off.
 */
public class InvoiceCalculator {

    /** One row on the invoice. */
    public record LineItem(String product, int qty, double unitPrice) {}

    /** Discount fraction for a quantity, e.g. 0.05 means 5% off. */
    public static double quantityDiscount(int qty) {
        if (qty >= 50) {
            return 0.10;
        }
        if (qty >= 10) {
            return 0.05;
        }
        return 0.0;
    }

    /** Grand total including tax, rounded to 2 decimals. */
    public static double totalWithTax(List<LineItem> items, double taxRate) {
        double subtotal = 0.0;
        for (LineItem item : items) {
            double gross = item.qty() * item.unitPrice();
            subtotal += gross * (1 - quantityDiscount(item.qty()));
        }
        return round(subtotal * (1 + taxRate));
    }

    static double round(double value) {
        return Math.round(value * 100.0) / 100.0;
    }
}
