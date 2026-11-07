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