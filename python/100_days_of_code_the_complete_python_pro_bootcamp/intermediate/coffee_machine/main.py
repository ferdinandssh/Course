MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report(resource,money):
    for bahan in resource:
        sisa = resource[bahan]
        if bahan == 'coffee':
            satuan = 'g'
        else:
            satuan = 'ml'
        print( f'{bahan}: {sisa}{satuan}')
    print(f'Money: ${money}')


def transaction(resource,input,coin):
    global profit
    check = MENU[input]
    ingredient = check["ingredients"]
    cost = check['cost']
    is_sufficient = True
    old_resource = resource.copy()
    old_profit = profit
    for bahan in resource:
        if ingredient[bahan] > resource[bahan]:
            print(f'Sorry there is not enough {bahan}')
            is_sufficient = False
        else:
            resource[bahan] = old_resource[bahan] - ingredient[bahan]    
    if cost > coin:
        print(f'Sorry there is not enough money. Money refunded')
        is_sufficient = False
    elif coin >= cost and is_sufficient == True:
        profit += cost    
        change = round(coin-cost,2)        
        print(f'You paid ${coin}. It cost ${cost}. Money change ${change}') 

        print("Report before transaction")
        print_report(old_resource,old_profit)

        print("Report after transaction")
        print_report(resource,profit)

        print(f'Transaction successful. {input} served')

def input_coin():
    q = float(input('how many quarters?: '))
    d = float(input('how many dimes?: '))
    n = float(input('how many nickles?: '))
    p = float(input('how many pennies?: '))
    total_coin = q*0.25 + d*0.1 + n*0.05 + p*0.01
    return total_coin


def coffee_shop():
    menu_list = list(MENU.keys())
    is_on = True
    while is_on:        

        is_valid_input = False
        while not is_valid_input:
            inputs = input("What would you like? (espresso/latte/cappuccino): ")
            if inputs.lower() in menu_list or inputs.lower() == "off" or inputs.lower() == "report":
                is_valid_input = True
                if inputs.lower() == 'off':
                    print("Turn off coffee machine")
                    is_on = False
                elif inputs.lower() == 'report':
                    print_report(resources,profit)
                else:                    
                    transaction(resources,inputs,input_coin())                    
            else:                
                print("Invalid input. Please try again")

coffee_shop()
# check_sufficient(resources,'latte',input_coin())


# transaction(resources,'latte',input_coin())
