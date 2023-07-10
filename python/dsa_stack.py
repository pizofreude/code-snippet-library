# Here's a Python code snippet that demonstrates the implementation of a stack data structure using a list:

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack size:", stack.size())
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())


# In this code snippet, we define a `Stack` class that implements the stack data structure.
# The stack is implemented using a list, where the top of the stack is the last element of the list.

# The `Stack` class provides the following methods:
# - `push(item)`: Pushes an item onto the top of the stack.
# - `pop()`: Removes and returns the top item from the stack.
# - `peek()`: Returns the top item of the stack without removing it.
# - `is_empty()`: Checks if the stack is empty.
# - `size()`: Returns the number of items in the stack.

# We demonstrate the usage of the `Stack` class by creating a stack object, pushing some elements onto the stack,
#  and performing operations such as checking the stack size, retrieving the top element, and popping an element from the stack.

# You can further explore data structures and algorithms by implementing other data structures like queues, linked lists, or trees,
#  and experimenting with different algorithms like binary search, depth-first search, or dynamic programming.