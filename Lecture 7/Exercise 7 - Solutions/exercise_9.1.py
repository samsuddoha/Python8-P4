#finding the max number without using function

n=int(input("Enter the value of n: "))
numbers=[]
for i in range(n):
    num=int(input(f"Enter number {i+1}: "))
    numbers.append(num)
#finding the max number 
max_num=-1000
for x in numbers:
    if x>max_num:
        max_num=x
print(f"The maximum Number is: {max_num}")