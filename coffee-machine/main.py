
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
profit = 0

def generate_report():
    """Generate the report for the owner"""
    print(f"""
    Water: {resources["water"]}
    Milk : {resources["milk"]}
    Coffee : {resources["coffee"]}
    Money: {profit}
        """)
def is_resource_sufficient(order_ingredients):
    """Check if the resource is sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    
    return True

def process_transaction(drink_cost):
    print("please insert coins")
    total = 0
    total += int(input("How many quarters ?")) * 0.25
    total += int(input("How many dimes ? ")) * 0.1
    total += int(input("How many nickles ?")) * 0.05
    total += int(input("How many pennies ?")) * 0.01

    if total > drink_cost:
        print(f"Here is ${round(total - drink_cost,2)} dollars in change")
        return True
    elif total ==  drink_cost :
        return True
    else :
        print(f"Sorry, that's not enough ${total} money. you need to pay ${drink_cost}.")
        return False

def make_coffee(drink_name, menu_choice):
    ingredients = menu_choice["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink_name}. Enjoy!")


is_machine_on = True
coffee_menu = ["espresso", "latte", "cappuccino"]
while is_machine_on:
    choice = input(f"What would you like? : \n {coffee_menu}\n").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        # call the function for report generation
        generate_report()
    elif choice in coffee_menu:
        drink = MENU[choice]
        # check the resources are sufficient
        if is_resource_sufficient(drink["ingredients"]) and process_transaction(drink["cost"]):
            profit += drink["cost"]
            make_coffee(choice, drink)
    else:
        print("Sorry, that's not a valid choice")


