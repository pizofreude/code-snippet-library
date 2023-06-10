import datetime

date_string = "2023-06-09"
formatted_date = datetime.datetime.strptime(date_string, "%Y-%m-%d").strftime("%d-%m-%Y")

print(formatted_date)


# This is Python code that converts a date string from one format to another.

# The `import` statement imports the `datetime` module.

# The `date_string` variable contains a string representation of a date in the format "YYYY-MM-DD".

# The `datetime.datetime.strptime` function parses the date string and returns a datetime object.
# The first argument is the date string to parse, and the second argument is the format of the date string.

# The `strftime` method formats the datetime object as a string. The argument specifies the desired output format.

# The formatted date is assigned to the `formatted_date` variable.

# The `print` statement prints the formatted date to the console.

# In this case, the input date string "2023-06-09" is converted to "09-06-2023".