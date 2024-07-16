"""
Arrange a list of 0s and 1s such that all 0s comes first and all 1s come after?

Don't use built-in operator or don't create new list.

Example1 = [0, 1, 1, 0, 1, 0]
Example2 = [1, 0, 0, 1, 0, 1, 1, 0]
"""

def arrange_zeros_ones(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        while left < right and lst[left] == 0:
            left += 1
        while left < right and lst[right] == 1:
            right -= 1
        
        if left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1

    return lst


lst1 = [0, 1, 1, 0, 1, 0]
lst2 = [1, 0, 0, 1, 0, 1, 1, 0]

sorted_list1 = arrange_zeros_ones(lst1)
sorted_list2 = arrange_zeros_ones(lst2)

print(sorted_list1) #OUTPUT: [0, 0, 0, 1, 1, 1]
print(sorted_list2) # OUTPUT: [0, 0, 0, 0, 1, 1, 1, 1]