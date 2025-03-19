import sys

def up():
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].upper())

up()
