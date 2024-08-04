from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    menu_list = menu.get_items()
    is_valid_choice = False
    while not is_valid_choice:
        choice = input(f"What would you like? (espresso/latte/cappuccino): ")
        if choice.lower() in menu_list or choice.lower() == "off" or choice.lower() == "report":
            is_valid_choice = True
        else:
            print("Invalid input. Try again!")            
    if choice == "off":
        print("Turn off the machine")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)