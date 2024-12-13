#counting the odd and even numbers

numbers=[23, 12, 34, 2, 33, 5, 6]
odd=0
even=0
for n in numbers:
    if n%2==0:
        even+=1
    elif n%2==1:
        odd+=1
print(f"The odd number is: {odd} and even number is: {even}")
