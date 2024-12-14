
# Take the number of scores
n = int(input("Enter the number of students: "))
scores = []
for i in range(n):
    score = float(input(f"Enter score for student {i + 1}: "))
    scores.append(score)

# Find the maximum score
max_score=-1000
for score in scores:
    if score>max_score:
        max_score=score
#you can use the max score directly
#max_score = max(scores)

# Calculate the percentage increase needed to raise the maximum score to 100
percentage_increase = 100 / max_score

# Adjust all scores
final_score=[]
for n in scores:
    n= round(n*percentage_increase,2)
    if n<60:
        n=60
    final_score.append(n)

# Print the final scores
print(f"Original scores: {scores}")
print(f"Adjusted scores: {final_score}")
