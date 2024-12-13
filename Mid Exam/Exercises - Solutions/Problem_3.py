txt = input("Enter a String: ")

lowercase_string = txt.lower()

vowels = "aeiou"
vowel = 0
for char in lowercase_string:
    if char in vowels:
        vowel += 1

string_list = list(lowercase_string)
string_list.reverse()
reversed_string = ''.join(string_list)

print(f"Lowercase: {lowercase_string}")
print(f"Number of vowels: {vowel}")
print(f"Reversed string: {reversed_string}")
