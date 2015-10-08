#!/usr/bin/python
import os
from sys import argv

def usage():
	print("USAGE: %s [symbol_name]" % argv[0])
	exit()

symbol_name = ""
if len(argv) > 1:
	try:
		symbol_name = argv[1]
		if symbol_name == "":
			raise
	except:
		usage()
print("====== " + symbol_name + " ======") 
os.system('grep ' + symbol_name + ' data.txt | awk \'$3 == "nr_threads" {print "0x"$1}\'')
