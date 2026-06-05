from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

input_choice = input(f"What would you like? {menu.get_items()}: ").lower()
is_on = True

while is_on:
    input_choice = input(f"What would you like? {menu.get_items()}: ").lower()
    if input_choice == "report":
        print(f"{coffee_maker.report(), money_machine.report()}")
    elif input_choice == "off":
        is_on = False
    else:
        drink = menu.find_drink(input_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
