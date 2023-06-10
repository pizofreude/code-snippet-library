import hashlib

password = "password123"
salt = "randomsalt"

# Generate a salted hash of the password
hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()

# Check if a provided password matches the stored hashed password
def check_password(password, stored_password):
    return hashlib.sha256((password + salt).encode()).hexdigest() == stored_password

# Example usage
stored_password = hashed_password
is_valid = check_password("password123", stored_password)
print(f"Password is valid: {is_valid}")

# This is Python code that demonstrates how to generate a salted hash of a password and check if a provided password matches the stored hashed password.

# The `import` statement imports the `hashlib` module.

# The `password` variable contains a plain-text password.

# The `salt` variable contains a random salt value.

# The `hashlib.sha256((password + salt).encode()).hexdigest()` statement generates a salted hash of the password using the SHA-256 algorithm.

# The `check_password` function takes a plain-text password and a stored hashed password as arguments.
# It generates a salted hash of the provided password and checks if it matches the stored hashed password.

# The example usage code stores the hashed password in the `stored_password` variable.
# It then calls the `check_password` function with the plain-text password "password123" and the stored hashed password. The result is printed to the console.
