n = int(input("Enter items of list: "))
numbers=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    numbers.append(num)
print(f"Enter numbers: {numbers}")
i = 0
while i < len(numbers):
    num = numbers[i]
    while numbers.count(num) > 1:
        numbers.remove(num)
    i += 1
print(f"List after removing duplicates: {numbers}")