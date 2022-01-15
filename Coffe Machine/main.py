import sys
import Menu
cost = 0
money_amount = 0
order_water_amount = 0
order_milk_amount = 0
order_coffee_amount = 0
current_resources = Menu.resources
water_amount = int(current_resources["water"])
milk_amount = int(current_resources["milk"])
coffee_amount = int(current_resources["coffee"])

def machine_resources():
    global current_resources
    global money_amount
    global water_amount
    global milk_amount
    global coffee_amount
    water_amount -= order_water_amount
    print(f"Water: {water_amount}ml")
    milk_amount -= order_milk_amount
    print(f"Milk: {milk_amount}ml")
    coffee_amount -= order_coffee_amount
    print(f"Coffee: {coffee_amount}g")
    money_amount += cost
    print(f"Money: {money_amount}$")

def count():
    print("Please insert coins.")
    dimes = int(input("How many dimes? ")) #Dime = 0.1$
    pennies = int(input("How many pennies? "))  #Penny = 0.01$
    nickles = int(input("How many nickles? "))  #Nickel = 0.05$
    quarters = int(input("How many quarters? "))  #Quarter = 0.25$
    coins = (quarters*0.25) + (nickles*0.05) + (pennies*0.01) + (dimes*0.1)
    money = round(coins, 3)
    print(f"Your total = {money}$")
    if cost > money:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = round(money - cost, 3)
        print(f"Here is your change: {change}$")



def coffee():
    global order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        global flag
        flag = False
    elif order == "report":
        machine_resources()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        global cost
        global order_water_amount
        global water_amount
        global order_milk_amount
        global order_coffee_amount
        cost = Menu.MENU[order]["cost"]
        order_water_amount = Menu.MENU[order]["ingredients"]["water"]
        order_milk_amount = Menu.MENU[order]["ingredients"]["milk"]
        order_coffee_amount = Menu.MENU[order]["ingredients"]["coffee"]
        if water_amount < order_water_amount:
            print("Sorry there is not enough water")
            coffee()
        if milk_amount < order_milk_amount:
            print("Sorry there is not enough milk")
            coffee()
        if coffee_amount < order_coffee_amount:
            print("Sorry there is not enough coffee")
            coffee()
        print(f"Cost will be {cost}$")
        count()
    else:
        print("Invalid Entry!")

flag = True
while flag == True:
    coffee()