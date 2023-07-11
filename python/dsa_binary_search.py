# Here's a Python code snippet that demonstrates the implementation of a binary search algorithm:


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
numbers = [2, 4, 7, 10, 13, 18, 21]
target = 13
index = binary_search(numbers, target)

if index != -1:
    print(f"Target found at index {index}")
else:
    print("Target not found")


# In this code snippet, we define a `binary_search` function that takes a sorted array `arr` and a target value as input.
# The function performs a binary search on the array to find the index of the target value.

# The binary search algorithm works by repeatedly dividing the search space in half until the target value is found or the search space is exhausted.
# In each iteration, we compare the middle element of the current search space to the target value and update the search space accordingly.

# The `binary_search` function returns the index of the target value if found, or -1 if the target value is not present in the array.

# We demonstrate the usage of the `binary_search` function by searching for a target value in an example sorted array.
# The function returns the index if the target is found, and we print the corresponding message accordingly.

# This code snippet illustrates a basic implementation of the binary search algorithm.
# We can further explore data structures and algorithms by implementing other search algorithms.
# E.g. linear search, binary search tree or tackling sorting algorithms (e.g., merge sort, quicksort) to deepen our understanding of how dsa works.