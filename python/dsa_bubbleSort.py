# Here's a Python code snippet that demonstrates a simple implementation of the bubble sort algorithm, which is a basic sorting algorithm:


def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage
numbers = [64, 34, 25, 12, 22, 11, 90, 1, 200]
bubble_sort(numbers)
print("Sorted array:", numbers)


# In this code snippet, we define a function `bubble_sort` that takes an array `arr` as input and performs the bubble sort algorithm on it.

# The bubble sort algorithm works by repeatedly swapping adjacent elements if they are in the wrong order until the entire array is sorted.
# The outer loop iterates `n-1` times, where `n` is the length of the array. The inner loop compares adjacent elements and swaps them if they are out of order.

# After sorting the array, we demonstrate the usage of the `bubble_sort` function by sorting an example array `numbers`. The sorted array is then printed to the console.

# This code snippet serves as a starting point to learn about algorithms and data structures in Python.
# You can explore more complex algorithms and data structures and implement them in Python to further deepen your understanding.