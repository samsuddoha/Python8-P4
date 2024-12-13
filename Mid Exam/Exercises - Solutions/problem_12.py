input_string = input("Enter a string: ")

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

result = ""

for char in input_string:
    if char not in punctuations:
        result += char

print(f"String without punctuation: {result}")
