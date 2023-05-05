
# Taking user inputs
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
annual_return = 0.04
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of your salary you want to save, as a decimal: "))

# Calculating down payment and monthly savings
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

# Initializing month counter
months = 0

# Looping until down payment is reached
while current_savings < down_payment:
    current_savings += monthly_saved + ((current_savings * annual_return) / 12)
    months += 1

# Outputting result
print("Number of months:", months)
