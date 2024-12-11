# Take name and token number as input
name = input("Enter your name: ")
token = int(input("Enter your token number: "))

# Determine seat status based on the token number
if token == 0:
    print(f"Sorry! {name}: No seat available for you.")
elif token % 2 != 0:
    print(f"{name}: your seat is confirmed.")
else:
    print(f"{name}: you are in waiting list.")