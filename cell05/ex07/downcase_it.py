import sys

def low():
    if len(sys.argv) != 2:
        print("none")
    else:
        print(sys.argv[1].lower())

low()
