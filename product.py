# Number of products
n = int(input())

items = []
discount_values = []

for i in range(n):
    name, price, discount = input().split(",")

    price = int(price)
    discount = int(discount)

    discount_amount = price * discount / 100

    items.append(name)
    discount_values.append(discount_amount)

# Find minimum discount amount
min_discount = min(discount_values)

# Print items with minimum discount
for i in range(n):
    if discount_values[i] == min_discount:
        print(items[i])