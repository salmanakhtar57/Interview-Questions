"""
Given two strings, check if they are anagrams to each other or not by comparing them.

Example1 = "abcd", "cbad" #output: anagrams
Example2 = "abcd", "cdaf" #output: not anagrams
"""

def check_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return "anagrams"
    else:
        return "not anagrams"
    
print(check_anagrams("abcd", "cbad"))
print(check_anagrams("abcd", "cdaf"))