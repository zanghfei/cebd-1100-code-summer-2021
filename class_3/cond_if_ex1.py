customer_type = "W"
invoice_total = 150.00
discount_percent = 0.0

if customer_type == "R" and invoice_total < 100:
    discount_percent = 0

if customer_type == "R" and (invoice_total >= 100 and invoice_total < 250):
    discount_percent = .1

if customer_type == "R" and invoice_total >= 250:
    discount_percent = .2

if customer_type == "W" and invoice_total < 500:
    discount_percent = .4

if customer_type == "W" and invoice_total >= 500:
    discount_percent = .5
