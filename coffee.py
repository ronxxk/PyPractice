from gamedata import MENU, resources
profit = 0


def prompt():
    prompt_is = input("What would you like? (espresso/latte/cappuccino):\n").lower()
    return prompt_is

def resource(prompt):

    cost_of_coffee = MENU[prompt]["cost"]
    water = resources["water"] - MENU[prompt]["ingredients"].get("water", 0)
    milk = resources["milk"] - MENU[prompt]["ingredients"].get("milk", 0)
    coffee = resources["coffee"] - MENU[prompt]["ingredients"].get("coffee", 0)
    money = profit + cost_of_coffee

    return cost_of_coffee, water, milk, coffee, money

def take_money(cost_of_coffee):

    print("Please insert coins\n")

    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    cost = (quarter * 0.25) + (dime * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    
    if cost < cost_of_coffee:
        return "Invalid amount"
    else:
        change = -(cost_of_coffee - cost)
        return change

on = True
resource_remain = (0, resources["water"], resources["milk"], resources["coffee"], profit)

while on:
    promptisequal = prompt()

    if promptisequal == "off":
        on = False

    elif promptisequal in MENU:
        # Check if ingredients are sufficient BEFORE proceeding
        needed = MENU[promptisequal]["ingredients"]
        if (resources["water"] < needed.get("water", 0) or
            resources["milk"] < needed.get("milk", 0) or
            resources["coffee"] < needed.get("coffee", 0)):
            print(f"Sorry, {promptisequal} is currently not available.")
        else:
            resource_remain = resource(promptisequal)
            handelMoney = take_money(resource_remain[0])
            print(f"Your change is ${handelMoney}")
            print(f"Here is your {promptisequal} ☕️. Enjoy!")

    elif promptisequal == "report":
        # Fixed: each index accessed separately
        print(f"Water: {resource_remain[1]}ml")
        print(f"Milk: {resource_remain[2]}ml")
        print(f"Coffee: {resource_remain[3]}g")
        print(f"Money: ${resource_remain[4]}")

    else:
        print("Invalid choice")