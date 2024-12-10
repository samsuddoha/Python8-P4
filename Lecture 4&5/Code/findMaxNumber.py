#find the max number among three numbers

a,b,c=map(int,input("Enter three numbers (Space seperated):").split())
if a>b and b>c:
    print(f"The largest number is: {a}")
elif b>a and b>c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")