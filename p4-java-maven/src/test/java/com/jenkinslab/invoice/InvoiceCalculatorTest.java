package com.jenkinslab.invoice;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.List;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

class InvoiceCalculatorTest {

    @Test
    @DisplayName("no discount below 10 units")
    void noDiscount() {
        var items = List.of(new InvoiceCalculator.LineItem("Mug", 4, 5.0));
        assertEquals(20.0, InvoiceCalculator.totalWithTax(items, 0.0));
    }

    @Test
    @DisplayName("5% discount at 10 units")
    void fivePercentDiscount() {
        var items = List.of(new InvoiceCalculator.LineItem("Mug", 10, 5.0));
        // 50.0 * 0.95 = 47.5
        assertEquals(47.5, InvoiceCalculator.totalWithTax(items, 0.0));
    }

    @Test
    @DisplayName("10% discount at 50 units")
    void tenPercentDiscount() {
        var items = List.of(new InvoiceCalculator.LineItem("Mug", 50, 2.0));
        // 100.0 * 0.90 = 90.0
        assertEquals(90.0, InvoiceCalculator.totalWithTax(items, 0.0));
    }

    @Test
    @DisplayName("tax is applied after discounts and rounded to 2 decimals")
    void taxAndRounding() {
        var items = List.of(
                new InvoiceCalculator.LineItem("Mug", 3, 4.99),
                new InvoiceCalculator.LineItem("Beans", 2, 11.53));
        // subtotal 38.03 (3x4.99 + 2x11.53), tax 8% -> 41.0724 -> 41.07
        assertEquals(41.07, InvoiceCalculator.totalWithTax(items, 0.08));
    }

    @Test
    @DisplayName("an empty invoice totals zero")
    void emptyInvoice() {
        assertEquals(0.0, InvoiceCalculator.totalWithTax(List.of(), 0.08));
    }
}
