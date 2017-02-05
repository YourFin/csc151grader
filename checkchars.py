#!/bin/python3
import sys

with open(sys.argv[1], 'w') as jj:
    for arg in sys.argv[2:]:
         try:
             with open(arg, 'r') as ff:
                 over80cnt = 0
                 for line in ff:
                     if len(line) >= 80:
                         over80cnt+=1
                 jj.write(arg + "  ASS  " + str(over80cnt))
         except:
             print("error")

