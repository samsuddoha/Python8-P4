strings = ["radar", "hello", "level", "world", "madam", "python"]

palindromes = []

for string in strings:
    s_list = list(string)
    s_list.reverse()
    reversed_string = ''.join(s_list)
    if string == reversed_string:
        palindromes.append(string)

print(f"Palindromes in the list: {' '.join(palindromes)}")
