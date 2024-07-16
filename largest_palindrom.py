"""
Find the largest palindrome in a given string.

Example1 = "babad"
Example2 = "baabcaacbaabcaaca"
"""

def largest_palindrom(s):
    if s == "":
        return ""
    
    start, end = 0, 0

    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i+1)
        max_len = max(len1, len2)

        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2


    return s[start: end + 1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


s1 = "babad"
print(largest_palindrom(s1))

s2 = "baabcaacbaabcaaca"
print(largest_palindrom(s2))