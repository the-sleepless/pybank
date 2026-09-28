from src.actions import withdrawAction, depositAction, viewAction, exitAction
from utils.terminalUtils import tmessage
from utils.inputUtils import getInput
from collections.abc import Callable
from dataclasses import dataclass

@dataclass
class MainOption:
    name: str
    action: Callable[[], None]


mainOptions: dict[int, MainOption] = {
    1: MainOption("Withdraw", withdrawAction),
    2: MainOption("Deposit", depositAction),
    3: MainOption("View", viewAction),
    4: MainOption("Exit", exitAction),
}


while True:
    title = " "
    for index in mainOptions:
       item = mainOptions[index]
       title += f"({index}) {item.name} "

    tmessage(title + "\n", 0)
    selected = getInput("int")

    if selected is None or selected not in mainOptions:
        tmessage("Enter a valid input!")
        continue

    selectedItem = mainOptions[selected]
    selectedItem.action()
