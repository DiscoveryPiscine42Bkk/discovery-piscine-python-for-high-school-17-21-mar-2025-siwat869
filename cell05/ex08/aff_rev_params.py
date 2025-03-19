import sys

if len(sys.argv) < 3:
    print("none")  
else:
    
    print((sys.argv[1:][::-1]))