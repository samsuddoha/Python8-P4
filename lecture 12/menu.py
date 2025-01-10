def add_asif():
    print("I am from add_asif")
def display_asif():
    print("I am from display_asif")
def search_asif():
    print("I am from search_asif")


while True:
    print("\nStudent Information System")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student by ID or Name")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_asif()
    elif choice == 2:
        display_asif()
    elif choice == 3:
        search_asif()
    elif choice == 4:
        print("Update")
    elif choice == 5:
        print("Delete")
    elif choice == 6:
        print("Bye bye... Have a nice day...")
        break
    else:
        print("invalid choice")