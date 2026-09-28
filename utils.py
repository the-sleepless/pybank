import time

from terminal import tprint, tloading, tclear

def number(value):
    try:
        value = int(value)

        return value
    except ValueError:
        tprint("Select a valid input.", loading=False, clear=True)
        time.sleep(2)

        return None
