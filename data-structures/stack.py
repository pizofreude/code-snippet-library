class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.size())


# The Python code defines a Stack class. A stack is a data structure that follows the Last-In-First-Out (LIFO) principle.

# The __init__ method initializes the stack with an empty list. The push method adds an item to the top of the stack.

# The pop method removes and returns the top item from the stack if it is not empty. The is_empty method returns True if the stack is empty and False otherwise.

# The size method returns the number of items in the stack.

# The example usage creates a new stack object, pushes three items onto the stack, pops an item from the stack (which should return 3),
# and prints the size of the stack (which should be 2).