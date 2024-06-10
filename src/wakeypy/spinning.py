# -*- coding: utf-8 -*-
import secrets
import time

import tomllib
from rich.console import Console
from wakepy import keep

console = Console(width=80)

with open(
    "/Users/evanbaird/Projects/Projects/wakeypy/pyproject.toml",
    mode="rb",
) as fp:
    loading = tomllib.load(fp)
    version = "v." + loading["tool"]["poetry"]["version"]


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


status = " [green]Press Ctrl-C to exit[/green]"


def rando_dots():
    return "dots" + str(secrets.choice(range(2, 9)))


with console.status(status, spinner=rando_dots()):
    console.print(
        rf"""
                       _
                      | |
    __        __ __ _ | | __ ___  _   _  _ __    _   _
    \ \  /\  / // _` || |/ // _ \| | | || '_  \ | | | |
     \ \/  \/ /| (_| ||   <|  __/| |_| || |_)  || |_| |
      \__/\__/  \__,_||_|\_\\___| \__, || .___/  \__, |
      {version}                      __/ || |       __| |
                                  |___/ |_|      |___/
    """,
        style="bold magenta",
    )
    console.print(
        ":white_heavy_check_mark: System will continue running program\n"
        ":white_heavy_check_mark: Presentation mode is on. Screensaver and Screenlock will be prevented.",
        style="green",
    )
    {do_something()}
