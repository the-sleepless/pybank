import time

from wallet import deposit, withdraw, view, money
from terminal import tprint, tloading, tclear

options = {
    1: "Withdraw",
    2: "Deposit",
    3: "View"
}

wallet_options = {
    1: "Bank",
    2: "Wallet"
}


while True:
    tprint(f"Select an option: (1): {options[1]} | (2) {options[2]} | (3) {options[3]}", loading=True)
    option = input("> ")

    if not option.isdigit() or not int(option) in options:
        tprint("Select a valid option.", loading=False, clear=True)
        time.sleep(2)
        continue
    else:
        option = int(option)

    if option == 1:
        tprint("Enter an amount:")
        amount = input("> ")

        if not amount.isdigit() or int(amount) > money["Bank"]:
            tprint("Select a valid amount.", loading=False, clear=True)
            time.sleep(2)
            continue

    elif option == 3:
        tprint(f"Select an option: (1): {wallet_options[1]} | (2) {wallet_options[2]}", loading=True)
        tmp = input("> ")

        if not tmp.isdigit() or not int(tmp) in wallet_options:
            tprint("Select a valid option.", loading=False, clear=True)
            time.sleep(2)
            continue
        else:
            tprint(f"Your balance in {wallet_options[int(tmp)]} is {view(wallet_options[int(tmp)])}")
            time.sleep(2)
