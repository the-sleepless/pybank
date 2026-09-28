import json


def load_data() -> dict[str, int]:
    with open("localStorage.json", "r") as file:
        return json.load(file)


def save_data(data: dict[str, int]):
    with open("localStorage.json", "w") as file:
        json.dump(data, file, indent=4)
