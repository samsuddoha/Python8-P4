# Taking the number of inputs
n = int(input("Enter how many numbers you want to input: "))

# Taking n numbers as input and storing them in a list
numbers = list(map(int, input(f"Enter {n} numbers separated by space: ").split()))

# Printing the list of numbers
print("The list of numbers is:", numbers)

n=int(input("Enter how many number you want to input: "))
numbers=list(map(int,input(f"Enter{n} numbers seperated by space:").split()))
print(numbers)

#using loop
n=int(input("Enter the value of n: "))
numbers=[]
for i in range(n):
    num=int(input(f"Enter number{i+1}: "))
    numbers.append(num)
print(numbers)