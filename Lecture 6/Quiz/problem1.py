# Sample input list
students = [95, 87, 72, 68, 91]

# Initialize counters for each category
gold_count = 0
silver_count = 0
bronze_count = 0
participation_count = 0

# Classify each student based on their score
for score in students:
    if score > 90:
        gold_count += 1
    elif 80 <= score <= 90:
        silver_count += 1
    elif 70 <= score < 80:
        bronze_count += 1
    else:
        participation_count += 1

# Print the results
print(f"Gold Medal: {gold_count} students")
print(f"Silver Medal: {silver_count} students")
print(f"Bronze Medal: {bronze_count} students")
print(f"Participation Award: {participation_count} students")
