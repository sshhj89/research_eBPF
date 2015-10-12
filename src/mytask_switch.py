#!/usr/bin/python
# Copyright (c) PLUMgrid, Inc.
# Licensed under the Apache License, Version 2.0 (the "License")

from bcc import BPF
from time import sleep

CPUNUM = 8
b = BPF(src_file="mytask_switch.c")
b.attach_kprobe(event="finish_task_switch", fn_name="count_sched")

sleep(1)

totalCountPerCPU = {}
totalCountPerCPU.clear()

for k, v in b["stats"].items():
    print("cpu: %d, pid: %d, switched count: %d" % (k.cpu, k.pid,v.value))
    if(totalCountPerCPU.get(k.cpu,None) is None):
	totalCountPerCPU[k.cpu] = v.value
    else:
	totalCountPerCPU[k.cpu] += v.value;

print "=======  total switched count per CPU ========"; 

for k, v in totalCountPerCPU.items():
	print("cpu: %d, performed count: %d" % (k,v)) 
