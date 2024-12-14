numbers=list(map(int,input("Enter numbers: ").split()))
odd_sum=0
even_sum=0
for num in numbers:
    if num%2==0:
        even_sum+=num
    elif num%2==1:
        odd_sum+=num

print(f"Sum of even numbers is: {even_sum}")
print(f"Sum of od numbers is: {odd_sum}")
max_num=max(odd_sum,even_sum)
print(f"maximum number between two sum is: {max_num}")
