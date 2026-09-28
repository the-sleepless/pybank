from typing import Literal

money = {
    "Bank": 500,
    "Wallet": 0,
}



def view(option: str):
    return money[option]



def withdraw(value: int | float):
    if money["bank"] < value:
        return False, "Insufficient balance for withdrawal."



def deposit(value: int | float):
    if money["wallet"] < value:
        return False, "Insufficient balance for deposit."
