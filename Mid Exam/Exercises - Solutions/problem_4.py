first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

print(f"Prime numbers between {first} and {second}: ", end="")

for num in range(first, second + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
