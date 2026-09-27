from typing import Literal

money = {
    "bank": 0,
    "wallet": 0,
}



def view(option: Literal["bank", "wallet"]):
    return money[option]



def withdraw(value):
    if money["bank"] < value:
        return False, "Insufficient balance for withdrawal."



def deposit(value):
    if money["wallet"] < value:
        return False, "Insufficient balance for deposit."
