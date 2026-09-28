import subprocess
import colors
import time
import os


def tclear():
    subprocess.run(["cls" if os.name == "nt" else "clear"])


def tloading(clear: bool = True):
    loading = "[ • • • • • • • • • • ]"

    if clear:
        tclear()

    for char in loading:

        if char != "•":
            continue

        loading = loading.replace("•", f"{colors.GREEN}#{colors.RESET}", 1)
        print(loading, end="\r", flush=True)
        time.sleep(0.05)


def message(text: str, duration: int = 2):
    tprint(text)
    time.sleep(duration)


def tprint(text: str, loading: bool = False, clear: bool = True):
    if loading:
        tloading(clear)
    elif clear:
        tclear()

    print_text = ""

    for char in text:
        print_text += char
        print("\r\033[K" + print_text, end="", flush=True)
        time.sleep(0.01)

    print()
