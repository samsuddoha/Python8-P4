nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = []

for sublist in nested_list:
    for item in sublist:
        flattened_list.append(item)

print(f"Flattened List: {flattened_list}")
