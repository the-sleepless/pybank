from typing import Literal
from utils import numberUtils

def getInput(type: Literal["str", "int"]):
    text = input(" | > ")

    if type == "int":
        result = numberUtils.toNumber(text)

        if result is None:
            # colocar a mensagem de erro dps
            return

        return result

    if type == "str":
        return
