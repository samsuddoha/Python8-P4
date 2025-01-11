def isPalindrome(s):

    rev = ''.join(reversed(s))

    if (s == rev):
        return True
    return False
# main function
s = "madam"
ans = isPalindrome(s)

if (ans):
    print("Yes! it's a palindrome")
else:
    print("No! it's not a palindrome")