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


def check_resources(drink_resources):
    for item in drink_resources:
        if resources[item] >= drink_resources[item]:
            return True
        else:
            print(f"Sorry I don't have enough {item}")
            return False


def take_coins():
    print("Please insert coins: ")
    total = int(input("How many quarters ")) * 0.25
    total += int(input("How many dimes ")) * 0.10
    total += int(input("How many nickels ")) * 0.05
    total += int(input("How many pennies ")) * 0.01
    return total


def process_payment(total, drink_cost):
    if total >= drink_cost:
        global profit
        profit += drink_cost
        change = round(total - drink_cost, 2)
        if change > 0:
            print(f"Here is your change: {change}")
        return True
    else:
        print(f"Sorry but {total} is not enough money. Here is a refund.")
        return False


def make_coffee(drink_choice, drink_ingredients):
    print(f"Here is your {drink_choice}, please enjoy!")
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


profit = 0

is_on = True
while is_on:
    choice = input("What coffee would you like? (espresso/latte/cappuccino) ")
    if choice == "off":
        print("Goodbye!")
        is_on = False
    elif choice == "report":
        print(f"Milk: {resources['milk']}ml")
        print(f"Water: {resources['water']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: {profit}")
    else:
        drink = MENU[choice]
        enough_resources = check_resources(drink["ingredients"])
        if enough_resources:
            print("Excellent choice. ")
            payment = take_coins()
            if process_payment(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
