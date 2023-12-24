# Load
with open("/proc/loadavg", "r") as f:
    print("Average Load: " + f.read().split(" ")[0])
