# Claire Sandy
# 10/02/2026
# end of week assignment, week 6

# Excersize 1

employees = ["Bob", "Carlos", "Alice"]
print(employees)

employees.append("Dana")
print(employees)

employees.remove("Bob")
print(employees)

employees.insert(0, "Evelyn")
print(employees)

# sort alphabetically
employees.sort()
print(employees)

# Excersize 2

ratings = [5, 4, 3, 5, 5, 5, 2, 3, 3, 3, 3, 2, 5, 4, 3]

# five star ratings
print(5 in ratings)
print(ratings.count(5))

# average rating
print(sum(ratings) / len(ratings))

# ones
if 1 in ratings:
    print("Low rating exists.")
else:
    print("No 1-star ratings found.")

    # Excersize 3

# ascending order
stock = [120, 45, 300, 53, 90, 6, 200, 108, 43, 2]
stock.sort()
print(stock)

# descening order
stock.sort(reverse=True)
print(stock)

# Excersize 4

revenue = [
    12000,
    15000,
    14000,
    16000,
    18000,
    17000,
    20000,
    21000,
    19000,
    22000,
    23000,
    24000,
]

q1 = revenue[0:3]
q2 = revenue[3:6]
q3 = revenue[6:9]
q4 = revenue[9:12]

# printing reveues
print("Q1:", q1)
print("Q1 Total Revenue: ${:,}".format(sum(q1)))
print("Q1 Monthly Average: ${:,.2f}".format(sum(q1) / len(q1)))

print("Q2:", q2)
print("Q2 Total Revenue: ${:,}".format(sum(q2)))
print("Q2 Monthly Average: ${:,.2f}".format(sum(q2) / len(q2)))

print("Q3:", q3)
print("Q3 Total Revenue: ${:,}".format(sum(q3)))
print("Q3 Monthly Average: ${:,.2f}".format(sum(q3) / len(q3)))

print("Q4:", q4)
print("Q4 Total Revenue: ${:,}".format(sum(q4)))
print("Q4 Monthly Average: ${:,.2f}".format(sum(q4) / len(q4)))

# Excersize 5
import copy

customer_purchases = [
    "milk",
    ["milk", "bread", "eggs"],
    "bread",
    ["milk", "bread", "eggs", "tp"],
]

# number of customers
print("Number of customers:", len(customer_purchases))

for purchase in customer_purchases:
    if isinstance(purchase, list):
        if "tp" in purchase:
            print("tp was purchased")

    else:
        if purchase == "tp":
            print("tp was purchased")

# new copy
new_purchases = copy.deepcopy(customer_purchases)

for purchase in new_purchases:
    if isinstance(purchase, list):
        if "tp" in purchase:
            purchase[purchase.index("tp")] = "butter"

print("Orignal:", customer_purchases)
print("Copy:", new_purchases)
