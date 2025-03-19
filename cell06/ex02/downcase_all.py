#!/usr/bin/env python3
# Your method definition
import sys

def downcase(str):
    return str.lower() 

if len(sys.argv) == 2:
    print(downcase(sys.argv[1]))  
else:
    print("none") 
