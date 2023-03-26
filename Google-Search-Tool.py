import requests
from bs4 import BeautifulSoup

# Prompt the user for input
search_term = input("Enter a search term: ")

# Make a request to Google
url = "https://www.google.com/search?q=" + search_term
response = requests.get(url)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the search result links
links = soup.find_all("a")

# Write the links to a file
with open("google_search_results.txt", "w") as f:
    for link in links:
        href = link.get("href")
        if href.startswith("/url?q="):
            f.write(href[7:] + "\n")