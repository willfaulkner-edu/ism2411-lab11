# Excercise 1
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print(customer)
# Excercise 2

customer["phone"] = "555-0199"
print(customer)


customer["tier"] = "platinum"
print(customer)


del customer["email"]
print(customer)

# Excercise 3
email_result = customer.get("email", "no email on file")
print(email_result)

# Excercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key)

# Excercise 5
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}
purchase_amount = 200.00
discount_rate = tier_discounts.get(customer["tier"], 0)

discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print(f"Tier: {customer['tier']}")
print(f"Discount %: {discount_rate}")
print(f"Final price: ${final_price:.2f}")

# Excercise 6
customers_list = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"},
    {"name": "Diana", "tier": "bronze"}
]

purchase_amount = 300.00
for cust in customers_list:
    tier = cust["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * discount_rate
    print(f"Customer: {cust['name']} | Tier: {tier} | Discount: ${discount_amount:.2f}")

# Excercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK alert: {product_name} (Stock: {info['stock']})")

# Excercise 8
transactions = [
    {"region": "south", "amount": 300},
    {"region": "north", "amount": 150},
    {"region": "south", "amount": 200}
]
sales_summary = {}
for tx in transactions:
    reg = tx["region"]
    amt = tx["amount"]
    sales_summary[reg] = sales_summary.get(reg, 0) + amt

for reg in sorted(sales_summary):
    print(f"{reg}: {sales_summary[reg]}")