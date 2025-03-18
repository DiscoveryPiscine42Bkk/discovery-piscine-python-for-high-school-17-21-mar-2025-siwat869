original_array = [2, 8, 9, 48, 8, 22, -12, 2]
filtered_array = []
for num in original_array:
    if num > 5:
        filtered_array.append(num)

    
new_array = []
for num in filtered_array:
    new_array.append(num + 2)

    
print(original_array)
print(new_array)