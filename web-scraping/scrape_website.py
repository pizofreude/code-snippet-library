import requests
from bs4 import BeautifulSoup

# Send HTTP GET request to the website
response = requests.get("https://example.com")

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract specific data from the website
# ...

# Display the extracted data
# ...


# This is Python code that demonstrates how to send an HTTP GET request to a website, parse the HTML content using BeautifulSoup, and extract specific data from the website.

# The `import` statements import the necessary modules.

# The `requests.get("https://example.com")` statement sends an HTTP GET request to the website.

# The `BeautifulSoup(response.content, 'html.parser')` statement creates a BeautifulSoup object from the HTML content of the response.

# The code then extracts specific data from the website and displays it.