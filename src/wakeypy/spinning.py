from rich.console import Console
from wakepy import keep
import time


console = Console()


def do_something():
    """
    Running a simple subprocess to stay awake.
    :return:
    """
    with keep.presenting():
        while True:
            second = 60
            second += 10
            time.sleep(second)


status = "[green]Press Ctrl-C to exit[/green]"


with console.status(status, spinner='aesthetic'):
    do_something()
