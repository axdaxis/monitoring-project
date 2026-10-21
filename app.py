# i don't know what i'm doing
import psutil
import curses
import time
import math
import human_readable as hr
from curses import wrapper

def byteConvert(bytes):
    return hr.file_size(bytes)

# vars
active = True

def getData(dataType):
    match dataType:
        case "cpu":
            cpuPercent = psutil.cpu_percent(interval=None)
            return f"CPU avg: {str(cpuPercent)}%"
        case "memory":
            memDetails = psutil.virtual_memory()
            return f"RAM usage: {memDetails.percent}% ({byteConvert(memDetails.available)}/{byteConvert(memDetails.total)})"

def main(stdscr):
    stdscr.clear()
    # two windows horizontal.
    verticalSpace = math.floor((curses.LINES - 8))
    horizSpace = math.floor((curses.COLS - 8) / 2)
    windowOne = curses.newwin(
        verticalSpace,
        horizSpace,
        4,
        4
    )
    windowTwo = curses.newwin(
        verticalSpace,
        horizSpace,
        4,
        horizSpace + 4
    )
    windowTwo.box()
    windowTwo.addstr(2, 2, "Window 2")
    windowTwo.refresh()

    while active:
        windowOne.erase()
        windowOne.box()
        windowOne.addstr(2, 2, getData("cpu"))
        windowOne.addstr(3, 2, getData("memory"))
        time.sleep(1)
        windowOne.refresh()
    
wrapper(main)