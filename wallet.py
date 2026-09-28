import json

money: dict[str, int | float] = { "Bank": 0, "Wallet": 0 }

with open("data.json", "r") as file:
    money = json.load(file)

def view(option: str):
    return f"{money[option]}$"

def save_data():
    with open("data.json", "w") as file:
        json.dump(money, file, indent=4)

def withdraw(value: int | float):
    if money["Bank"] < value:
        return False, "Insufficient balance for withdrawal."

    money["Bank"] -= value
    money["Wallet"] += value

    save_data()

    return True, f"You withdrew {value}$ from the bank"

def deposit(value: int | float):
    if money["Wallet"] < value:
        return False, "Insufficient balance for deposit."

    money["Wallet"] -= value
    money["Bank"] += value

    save_data()

    return True, f"You deposited {value} into the bank."
