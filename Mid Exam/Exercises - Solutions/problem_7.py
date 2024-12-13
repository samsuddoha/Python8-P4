numbers = list(map(int, input("Enter a list of numbers: ").split(" ")))

numbers.sort(reverse=True)

if len(numbers) < 2:
    print("List must contain at least two numbers.")
else:
    largest = numbers[0]
    second_largest = None
    for num in numbers:
        if num < largest:
            second_largest = num
            break

    if second_largest is not None:
        print(f"Second largest number: {second_largest}")
    else:
        print("There is no second largest number, all elements are the same.")
