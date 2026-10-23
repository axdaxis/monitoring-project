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

def getData(dataType, disk=None):
    match dataType:
        case "cpu":
            cpuPercent = psutil.cpu_percent(interval=None)
            return f"CPU avg: {str(cpuPercent)}%"
        case "memory":
            memDetails = psutil.virtual_memory()
            return f"RAM usage: {memDetails.percent}% ({byteConvert(memDetails.available)}/{byteConvert(memDetails.total)})"
        case "disks":
            usage = psutil.disk_usage(disk.mountpoint)
            return (f"Usage on {disk.mountpoint}: {usage.percent}% ({byteConvert(usage.free)} free) ({byteConvert(usage.used)}/{byteConvert(usage.total)})")


def main(stdscr):
    stdscr.nodelay(True)
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


    while active:
        try:
            key = stdscr.getch()
        except curses.error:
            key = -1 
        if key == ord('q') or key == ord('Q'):
            break

        # windowOne
        windowOne.refresh()
        windowOne.erase()
        windowOne.box()
        # Clear out & style. Not ideal rendering every time but .erase does that
        
        windowTwo.box()
        windowTwo.addstr(2, 2, "Window 2")
        windowTwo.addstr(3, 2, "press q to quit")
        curses.setsyx(4, horizSpace + 4)
        windowTwo.refresh()

        # Add titlebar for windowOne
        windowOne.addstr(0, 2, "Performance Statistics")
        lineNum = 2

        # Get CPU stats
        windowOne.addstr(lineNum, 2, getData("cpu"))
        lineNum += 1

        # Get memory info
        windowOne.addstr(lineNum, 2, getData("memory"))
        lineNum += 1

        # Get how many drives are in system, move accordingly
        for i in psutil.disk_partitions(all=False):
            windowOne.addstr(lineNum, 2, getData("disks", i))
            lineNum += 1

        time.sleep(1)
    
wrapper(main)