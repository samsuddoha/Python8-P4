
# Take string input from user
string = input("Enter a sentence: ")

# Convert the string into a list of words
word_list = string.split()

# Print each word in lower and upper case
for word in word_list:
    print(f" {word.lower()} {word.upper()}")
