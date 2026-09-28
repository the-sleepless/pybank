from wallet import deposit, withdraw, view, money
from terminal import tprint, tloading, tclear, message
from utils import number

import time

options = {
    1: "Withdraw",
    2: "Deposit",
    3: "View",
    4: "Exit"
}

options2 = {
    1: "Bank",
    2: "Wallet"
}


while True:
    title = "Select an option | "
    for id, name in options.items():
        title += f"({id}): {name} | "

    tprint(title, loading=True)
    option = number(input("> "))

    if option is None or not option in options:
        continue


    if option == 1:
        tprint("Enter an amount:")
        amount = number(input("> "))

        if amount is None:
            continue

        success, msg = withdraw(amount)
        if not success:
            message(msg)
            continue

        message(msg)

    elif option == 2:
        tprint("Enter an amount:")
        amount = number(input("> "))

        if amount is None:
            continue

        success, msg = deposit(amount)
        if not success:
            message(msg)
            continue

        message(msg)

    elif option == 3:
        title = "Select an option | "
        for id, name in options2.items():
            title += f"({id}): {name} | "

        tprint(title, loading=True)
        tmp = number(input("> "))

        if tmp is None or not tmp in options2:
            continue

        message(f"Your balance in {options2[tmp].lower()} is {view(options2[tmp])}")

    elif option == 4:
        break

tprint("Execution finished", loading=True)
