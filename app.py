# i don't know what i'm doing
import psutil
import curses
from curses import wrapper

from datetime import datetime
import time
import math
import humanize

def byteConvert(bytes):
    return humanize.naturalsize(bytes, True)

# vars
active = True
warnLevel = 95
lineNum = 0
bootTime = psutil.boot_time()

def getData(dataType, disk=None):
    warning = False
    match dataType:
        case "cpu":
            cpuPercent = psutil.cpu_percent(interval=None)
            if cpuPercent >= warnLevel:
                warning = True
            return f"CPU avg: {str(cpuPercent)}%", warning
        case "memory":
            memDetails = psutil.virtual_memory()
            if memDetails.percent >= warnLevel:
                warning = True
            return f"RAM usage: {memDetails.percent}% ({byteConvert(memDetails.available)}/{byteConvert(memDetails.total)})", warning
        case "disks":
            usage = psutil.disk_usage(disk.mountpoint)
            if usage.percent >= warnLevel:
                warning = True
            return (f"Usage on {disk.mountpoint}: {usage.percent}% ({byteConvert(usage.free)} free) ({byteConvert(usage.used)}/{byteConvert(usage.total)})", warning)
        case "uptime":
            dtNow = datetime.now()
            dtUptime = datetime.fromtimestamp(bootTime)
            remainder = dtNow - dtUptime
            return f"Uptime: {humanize.precisedelta(remainder)} ago"

def addString(window, data, warning, x=2):
    global lineNum
    if warning:
        window.addstr(lineNum, x, data, curses.color_pair(1))
    else:
        window.addstr(lineNum, x, data)
    lineNum += 1

def main(stdscr):
    global lineNum
    # first initialization 
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
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
        cpu, warning = getData("cpu") 
        addString(windowOne, cpu, warning)

        # Get CPU stats
        mem, warning = getData("memory") 
        addString(windowOne, mem, warning)

        # Get uptime 
        uptime = getData("uptime") 
        addString(windowOne, uptime, False)

        # Get how many drives are in system, move accordingly
        for i in psutil.disk_partitions(all=False):
            diskData, warning = getData("disks", i)
            addString(windowOne, diskData, warning)

        time.sleep(1)
    
wrapper(main)