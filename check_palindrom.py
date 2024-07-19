"""
Checks if the given string s is a palindrome and return
"Palindrome" if it is, otherwise return "Not palindrome".

Example1: "racecar" #output: Palindrome
Example2: "hello" #Output: Not palindrome
"""

def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    

print(check_palindrome("racecar"))  # Output: "Palindrome"
print(check_palindrome("hello"))    # Output: "Not palindrome"