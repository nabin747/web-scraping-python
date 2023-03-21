import requests
from bs4 import BeautifulSoup

# URL of the New York Times website
url = "https://kathmandu.gov.np/official-type/elected-official-en/?lang=en"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article titles on the webpage
table = soup.find("tr")

data = []
for title in data:
    print(title[0])

# Print the titles
# for title in article_titles:
#     print(title.text.strip())
