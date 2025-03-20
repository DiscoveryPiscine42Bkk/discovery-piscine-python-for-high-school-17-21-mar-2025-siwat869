#!/usr/bin/env python3
import sys

def param():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")
param()
