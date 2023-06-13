import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the date and time
formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted date and time
print(f"Current date and time: {formatted_datetime}")


# This code snippet uses the datetime module in Python to retrieve the current date and time.

# It then formats the date and time using the strftime method, which allows you to specify the desired format.
# In this example, the format is set to "YYYY-MM-DD HH:MM:SS".

# Finally, the formatted date and time are printed to the console.