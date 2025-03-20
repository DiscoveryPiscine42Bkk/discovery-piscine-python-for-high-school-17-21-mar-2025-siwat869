#!/usr/bin/env python3
# Your method definition

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}.")
    else:
        print("Error! It was not a name.")

greetings("Alexandra")  
greetings("Wil")        
greetings()             
greetings(42)          
