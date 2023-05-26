import psutil
import time


def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print("CPU Usage: {}%".format(cpu_usage))
        # Perform additional analysis or actions based on the CPU usage
        time.sleep(5)


# Start continuous monitoring
monitor_cpu_usage()
