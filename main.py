import user_input
from utils import clear_console

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00,
}

MENU_ITEMS = [key for key in MENU]
COMMANDS = [*MENU_ITEMS, *["report", "off"]]
COIN_VALUE = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}


def show_report() -> None:
    print("-" * 40)
    for key in ["water", "milk", "coffee"]:
        print(f"{key.capitalize()}: {resources[key]}")

    print(f"Money: ${'{0:.2f}'.format(resources['money'])}")
    print("-" * 40)


def check_resources(drink: str) -> bool:
    ingredients = MENU[drink]["ingredients"]
    for key in ingredients:
        if resources[key] < ingredients[key]:
            print(f"Sorry! There is not enough {key}.")
            return False

    return True


def prepare_drink(drink: str) -> None:
    ingredients = MENU[drink]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]

    print(f"Here is your {drink}. Enjoy!")
    return None


def main():
    clear_console()

    running = True
    while running:
        drink_request = user_input.get(
            f"What would you like? ({ '/'.join(MENU_ITEMS) }): ",
            COMMANDS,
        )

        if drink_request == "off":
            print("Powering down.")
            running = False

        elif drink_request == "report":
            show_report()

        else:
            if check_resources(drink_request):
                drink_price = MENU[drink_request]["cost"]
                current_balance = 0.00

                print("Please insert coins:")
                for coin in ["quarters", "dimes", "nickels", "pennies"]:
                    coin_quantity = user_input.get_integer(f"How many {coin}?: ", min=0)
                    current_balance += coin_quantity * COIN_VALUE[coin]

                if drink_price <= current_balance:
                    user_change = current_balance - drink_price
                    if user_change > 0.00:
                        print(
                            f"Here is ${'{0:.2f}'.format(user_change)} dollars in change."
                        )

                    resources["money"] += drink_price
                    prepare_drink(drink_request)
                else:
                    print("Sorry! That's not enough money. Money refunded.")


if __name__ == "__main__":
    main()
