#!/bin/bash
#Sort by memory and show pid,ppid,cmd along with hostname
hostname
echo
ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem
