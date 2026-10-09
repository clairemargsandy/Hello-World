# Claire Sandy
# 09/03/2026
# EoW3

# Excersize 1 

import math

meal_price = float(input("Enter the price of the meal" ))

tip_percentage = float(input("Enter the tip percentage: "))

tip_decimal = tip_percentage / 100

tip_amount = meal_price * tip_decimal

total_bill = meal_price + tip_amount

rounded_total = math.ceil(total_bill)

print("Original amount:", meal_price)

print("Tip:", tip_amount)

print("Rounded total:", rounded_total)

# Excersize 2

meal_cost = 120

tax_percentage = 8

tip_percentage = 15

number_people = 4

total_cost_after_tax_tip = meal_cost * (1 + tax_percentage / 100) * (1 + tip_percentage / 100)

cost_per_person = total_cost_after_tax_tip / number_people

print("Total cost after tax and tip:", round(total_cost_after_tax_tip, 2))

print("Cost per person:", round(cost_per_person, 2))

#Excersize 3

total_budget = 50

item_cost = 3.49

tax_rate = 0.075

cost_with_tax = item_cost* (1 + tax_rate)

notebooks = int(total_budget / cost_with_tax)

money_left = total_budget - (notebooks * cost_with_tax)

print("You can afford:", notebooks)

print("Money left:", round(money_left, 2))


# Excersize 4

miles = float(input("How many miles will you travel? "))

miles_per_gallon = 30

cost_per_gallon = 3.75

gallons_needed = miles / miles_per_gallon

total_cost = gallons_needed * cost_per_gallon 

print("Total gallons needed: ", gallons_needed)

print("Total cost: ", round(total_cost, 2))

# Excersize 5
 
import random
 
dice_roll = random.randint(1, 10)

original_price = float(input("Enter the original price: "))

discount_percentage = dice_roll * 2

discount_amount = original_price * (discount_percentage / 100)

final_price = original_price - discount_amount

print("Original amount: ", original_price)

print("Discount amount: ", discount_amount)

print("Final price after discount: ", final_price)



 
 












