# verifying the eligibility of voting

age=int(input("Enter the age: "))
citizenship=input("Enter citizenship status (yes or no): ")

if age>=18 and citizenship=="yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")