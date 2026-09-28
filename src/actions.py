from utils.terminalUtils import tmessage
from utils.inputUtils import getInput
from src.transfer import view, getValue, deposit, withdraw

viewOptions = {
    1: "Bank",
    2: "Wallet"
}


def viewAction():
    title = " "
    for index in viewOptions:
        title += f"({index}) {viewOptions[index]} "

    tmessage(title + "\n", 0)
    selected = getInput("int")

    if selected is None or not selected in viewOptions:
        tmessage("Enter a valid input!")
        return

    tmessage(f"Your balance in {viewOptions[selected].lower()} is {view(viewOptions[selected])}")


def withdrawAction():
    tmessage("Enter a value:", 0)
    amount = getInput("int")

    if amount is None:
        tmessage("Enter a valid input!")
        return

    if getValue("Bank") < amount:
        tmessage("Insufficient balance!")
        return

    withdraw(amount)
    tmessage(f"You withdrew {amount} from the bank!")

def depositAction():
    tmessage("Enter a value:", 0)
    amount = getInput("int")

    if amount is None:
        tmessage("Enter a valid input!")
        return

    if getValue("Wallet") < amount:
        tmessage("Insufficient balance!")
        return

    deposit(amount)
    tmessage(f"You deposited {amount} into the bank!")


def exitAction():
    tmessage("Execution finished", 0)
    raise SystemExit
