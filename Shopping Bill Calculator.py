print("====== SHOPPING BILL CALCULATOR ======")

# Product 1
price1 = float(input("Enter price of product 1: "))
quantity1 = int(input("Enter quantity of product 1: "))

# Product 2
price2 = float(input("Enter price of product 2: "))
quantity2 = int(input("Enter quantity of product 2: "))

# Product 3
price3 = float(input("Enter price of product 3: "))
quantity3 = int(input("Enter quantity of product 3: "))

# Calculate individual totals
total1 = price1 * quantity1
total2 = price2 * quantity2
total3 = price3 * quantity3

# Calculate subtotal
subtotal = total1 + total2 + total3

# Discount
discount = subtotal * 0.10

# Amount after discount
amount = subtotal - discount

# GST (5%)
gst = amount * 0.05

# Final bill
final_bill = amount + gst

# Display bill
print("\n====== SHOPPING BILL ======")

print("Product 1 Total:", total1)
print("Product 2 Total:", total2)
print("Product 3 Total:", total3)

print("Subtotal:", subtotal)
print("Discount (10%):", discount)
print("GST (5%):", gst)

print("---------------------------")
print("Final Bill Amount:", final_bill)
print("===========================")
