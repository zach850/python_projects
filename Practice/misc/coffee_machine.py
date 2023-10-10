MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Ask user for input
coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

def coins(quarters, dimes, nickels, pennies):
    total = float(quarters * 0.25) + float(dimes * 0.10) + float(nickels * 0.05) + float(pennies * 0.01)
    return total

def track_resources(coffee_type):
    diff_dict = {}
    coffee_ingredients = MENU[coffee_type]['ingredients']

    # Calculate the difference between available resources and required ingredients
    for key in resources:
        if key in coffee_ingredients:
            diff_dict[key] = resources[key] - coffee_ingredients[key]
        else:
            diff_dict[key] = resources[key]

    return diff_dict
        

track_resources(coffee_type)

def coffee(coffee_type):
    if coffee_type not in MENU:
        print(f"Error: Coffee type '{coffee_type}' not found in MENU.")
        return None

    if coffee_type == coffee_type:
        print("Please insert your coins: " )
        quarters = float(input("how many quarters?: "))
        dimes = float(input("how many dimes?: "))
        nickles = float(input("how many nickles?: "))
        pennies = float(input("how many pennies?: "))
        total_money_added = coins(quarters, dimes, nickles, pennies)
        if total_money_added >= MENU[coffee_type]['cost']:
            change = round(total_money_added - MENU[coffee_type]['cost'],2)
            print(f"Here is {change} in change.")
            print(f"Here is your {coffee_type} ☕️. Enjoy!")
        else:
            print("Sorry, not enough money. Money refunded.")
            #TODO 
            #make function repeat with while loop 
        
        
