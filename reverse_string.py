"""
Return the reverse of string wihtout using built-in operator


Example1: "Hi, python developers!" Output: !srepoleved nohtyp ,iH
Example2: "AI/ML" Output: olleh
"""

def reverse_string(s):
    new_string = ""
    for char in s:
        new_string = char + new_string
    return new_string


reversed_str = reverse_string("Hi, python developers!")
print(reversed_str)  # Output: "!srepoleved nohtyp ,iH"

reversed_str = reverse_string("AI/ML")
print(reversed_str)  # Output: "LM/IA"