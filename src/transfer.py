from src.database import save_data, load_data
from typing import Literal

localStorage: dict[str, int] = load_data()


def view(option: str):
    return f"{localStorage[option]}$"


def getValue(option: Literal["Bank", "Wallet"]):
    return localStorage[option]


def withdraw(amount: int):
    localStorage["Bank"] -= amount
    localStorage["Wallet"] += amount

    save_data(localStorage)


def deposit(amount: int):
    localStorage["Wallet"] -= amount
    localStorage["Bank"] += amount

    save_data(localStorage)
