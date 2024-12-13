numbers = list(map(int, input("Enter numbers: ").split(" ")))

i = 0
while i < len(numbers):
    num = numbers[i]
    while numbers.count(num) > 1:
        numbers.remove(num)
    i += 1

sum = 0
for num in numbers:
    sum += num

average = sum / len(numbers)

print(f"Sum: {sum} and Average: {average:.2f}")
