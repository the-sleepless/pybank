import time
import colors

from terminal import tprint


def number(value: int | str):
    try:
        value = int(value)

        return value
    except ValueError:
        tprint(f"{colors.RED}Select a valid input.{colors.RESET}", loading=False, clear=True)
        time.sleep(2)
        return None
