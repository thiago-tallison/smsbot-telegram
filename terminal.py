import os


def clear_console():
    # Clear console command based on the operating system
    if os.name == "nt":  # for Windows
        _ = os.system("cls")
    else:  # for Unix-like systems (Linux, macOS, etc.)
        _ = os.system("clear")
