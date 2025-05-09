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
    "money": 0,
}

profit = 0


    

def is_resource_sufficient(order_ingredients):
    """Returns true if the resources are sufficient for the order, else returns false"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total amount of coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters would you like to insert? ")) * 0.25
    total += int(input("How many dimes would you like to insert? ")) * 0.1
    total += int(input("How many nickels would you like to insert? ")) * 0.05
    total += int(input("How many pennies would you like to insert? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Returns true if the transaction was successful, else returns false."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: €{change} and ")
        global profit
        profit += change
        return True
    else:
        print(f"Sorry, you don't have enough money.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")


is_on = True

while is_on:
    choice = input("What would you like to order? (espresso, latte, cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: €{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            print(f"Your drink costs: {drink["cost"]}")
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            

