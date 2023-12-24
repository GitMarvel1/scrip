import platform

# Architecture
print("Architecture: " + platform.architecture()[0])

# machine
print("Machine: " + platform.machine())

#release
print ("Release: " + platform.release())

#processor
print ("Processor :" + platform.processor())

# node
print("Node: " + platform.node())

# system
print("System: " + platform.system())

# distribution
#dist = platform.linux_distribution()
#dist = " ".join(x for x in dist)
#print("Distribution: " + dist)

# processor
print("Processors: ")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)
