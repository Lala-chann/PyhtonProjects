from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 2.0
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

# we have to write money outside of def, we have to calculate every time
money = 0

def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']

    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: {money}$"

def order_change(coffe_op,q,d,n,p):
    sum = q + d + n + p
    if coffe_op == "espresso":
        change = sum - MENU['espresso']['cost']
    elif coffe_op == "latte":
        change = sum - MENU['latte']['cost']
    else:
        change = sum - MENU['espresso']['cost']

    print(f"Here is ${change} in change")
    print(f"Here is your {coffe_op}☕. Enjoy!")

    return change

while True:
    option = input("What would you like? espresso/latte/capuccino: ").lower()
    if option == "report":
        print(report())

    if option == "espresso" or option == "latte" or option == "cappuccino":
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        sum = quarters + dimes + nickles + pennies

        order_change(option,quarters,dimes,nickles,pennies)


