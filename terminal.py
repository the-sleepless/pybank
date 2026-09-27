import subprocess
import time
import os


def clear():
    subprocess.run(["cls" if os.name == "nt" else "clear"])


def terminal_effect():
    loading = "[ • • • • • • • • • • ]"

    clear()

    for char in loading:
        loading = loading.replace("•", "#", 1)
        print(loading, end="\r", flush=True)
        time.sleep(0.05)
