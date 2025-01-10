import os

class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class StudentInfoSystem:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists("students.txt"):
            with open("students.txt", "r") as file:
                for line in file:
                    student_id, name, age, grade = line.strip().split(",")
                    self.students.append(Student(student_id, name, int(age), grade))

    def save_data(self):
        with open("students.txt", "w") as file:
            for student in self.students:
                file.write(f"{student.student_id},{student.name},{student.age},{student.grade}\n")

    def add_student(self, student_id, name, age, grade):
        student = Student(student_id, name, age, grade)
        self.students.append(student)
        self.save_data()

    def display_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                print(student)

    def search_student(self, search_term):
        found = False
        for student in self.students:
            if search_term.lower() in student.name.lower() or search_term == student.student_id:
                print(student)
                found = True
        if not found:
            print("Student not found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if age:
                    student.age = age
                if grade:
                    student.grade = grade
                self.save_data()
                print("Student information updated.")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_data()
                print("Student removed.")
                return
        print("Student not found.")

    def menu(self):
        while True:
            print("\nStudent Information System")
            print("1. Add Student")
            print("2. Display All Students")
            print("3. Search Student by ID or Name")
            print("4. Update Student Information")
            print("5. Delete Student")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                age = int(input("Enter Student Age: "))
                grade = input("Enter Student Grade: ")
                self.add_student(student_id, name, age, grade)

            elif choice == '2':
                self.display_students()

            elif choice == '3':
                search_term = input("Enter Student ID or Name to search: ")
                self.search_student(search_term)

            elif choice == '4':
                student_id = input("Enter Student ID to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                age = input("Enter new age (leave blank to keep current): ")
                grade = input("Enter new grade (leave blank to keep current): ")
                age = int(age) if age else None
                self.update_student(student_id, name if name else None, age if age else None, grade if grade else None)

            elif choice == '5':
                student_id = input("Enter Student ID to delete: ")
                self.delete_student(student_id)

            elif choice == '6':
                print("Exiting... Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentInfoSystem()
    system.menu()