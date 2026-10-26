# monitoring project
this is for a class. again.

---


# Python System Health & Telemetry Monitor

## Project Description

Develop a **Python command-line application** that monitors the health and performance of the computer it is running on. The application will collect live system telemetry, display it in an organized CLI interface, identify potential performance problems, and maintain a history of collected data.

The project should be divided into multiple Python files/modules rather than written entirely in one file.

## Project Requirements

The application must:

-   Monitor **CPU usage**
-   Monitor **RAM usage**
-   Monitor **disk usage**
-   Display **system uptime**
-   Display basic system information such as hostname, operating system, CPU cores, total RAM, and disk capacity
-   Automatically refresh telemetry at a set interval
-   Classify resource usage as **Normal, Warning, or Critical**
-   Allow warning/critical thresholds to be configured
-   Save telemetry readings to a log file
-   Calculate **minimum, maximum, and average** resource usage from collected readings
-   Provide a CLI menu for accessing monitoring, system information, statistics, and configuration
-   Handle errors or unavailable system information without crashing

## Suggested Advanced Features

After completing the required application, additional features may include:

-   Network upload/download monitoring
-   CPU temperature monitoring
-   Top CPU/RAM-consuming processes
-   Multiple-drive monitoring
-   CSV telemetry export
-   Custom monitoring intervals
-   Alert history

## Suggested Python Technologies

-   `psutil` — system telemetry
-   `platform` — operating system information
-   `socket` — hostname/network information
-   `json` — configuration storage
-   `csv` — telemetry logging

## Final Product

The completed project should function as a small **CLI-based system monitoring utility**, allowing a user to view the computer's current health as well as basic historical performance information.