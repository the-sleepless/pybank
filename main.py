import time

from wallet import deposit, withdraw, view, money
from terminal import tprint, tloading, tclear, message
from utils import number

options = {
    1: "Withdraw",
    2: "Deposit",
    3: "View"
}

options2 = {
    1: "Bank",
    2: "Wallet"
}


while True:
    tprint(f"Select an option: (1): {options[1]} | (2) {options[2]} | (3) {options[3]}", loading=True)
    option = number(input("> "))

    if option is None or not option in options:
        continue


    if option == 1:
        tprint("Enter an amount:")
        amount = number(input("> "))

        if amount is None:
            continue

     # finish later

    elif option == 2:
        tprint("Enter an amount:")
        amount = number(input("> "))

        if amount is None:
            continue

    # finish later

    elif option == 3:
        tprint(f"Select an option: (1): {options2[1]} | (2) {options2[2]}", loading=True)
        tmp = number(input("> "))

        if tmp is None or not tmp in options2:
            continue

        message(f"Your balance in {options2[tmp].lower()} is {view(options2[tmp])}")
