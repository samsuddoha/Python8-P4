num_students = int(input("Enter number of students: "))

names = []
tokens = []
scores = []

for i in range(num_students):
    details = input(f"Enter the name, token number, and score of student {i+1}: ")
    name, token, score = details.split(', ')
    names.append(name)
    tokens.append(int(token))
    scores.append(int(score))

print("Lucky students (prime token numbers):")
for i in range(num_students):
    token = tokens[i]
    if token > 1:
        is_prime = True
        for j in range(2, token):
            if token % j == 0:
                is_prime = False
                break
        if is_prime:
            print(f"Name: {names[i]}, Score: {scores[i]}")
