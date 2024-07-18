"""
Finding Pairs of Indices with a Target Sum.

Given an array of integers and a target integer, write a function find_indiced that returns a list of all 
pairs of indices whose corresponding elements in the array add up to the target value.

Example1 = ([2, 7, 11, 15], 9)  # Output: [(0, 1)]
Example2 = ([1, 2, 3, 4, 5, 6], 10)  # Output: [(3, 5), (4, 6)]

"""

def find_indices(arr, target):

    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append((i, j))

    return result


print(find_indices([2, 7, 11, 15], 9))  # Output: [(0, 1)]
print(find_indices([1, 2, 3, 4, 5, 6], 10)) #Output: [(3, 5)]