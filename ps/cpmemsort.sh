#!/bin/bash
#Sort by memory,cpu and show pid,ppid,cmd along with hostname
hostname
echo
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem --sort=-%cpu
