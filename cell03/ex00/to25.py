num = int(input("Enter a number less than 25: "))

if num > 25:
    print("Error")
else:
    for i in range(num, 26):
        print(i)
