#sum of all numbers from a list

#taking n input
n=int(input("Enter how many number you want to input: "))
numbers=list(map(int,input(f"Enter {n} numbers seperated by space:").split()))

#finding the sum
sum=0
for x in numbers:
    sum+=x
print(f"The sum is: {sum}")