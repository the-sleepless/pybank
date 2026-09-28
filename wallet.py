import json

money = { "Bank": 0, "Wallet": 0 }

with open("data.json", "r") as file:
    money = json.load(file)

def view(option: str):
    return money[option]

def save_data():
    with open("data.json", "w") as file:
        json.dump(money, file, indent=4)

def withdraw(value: int | float):
    if money["Bank"] < value:
        return False, "Insufficient balance for withdrawal."

def deposit(value: int | float):
    if money["Wallet"] < value:
        return False, "Insufficient balance for deposit."
