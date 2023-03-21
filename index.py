import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the website
url = 'https://baglungmun.gov.np/ne/elected-officials'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the data that you want to scrape
data = []
for row in soup.find_all('tr'):
    cells = row.find_all('td')
    if cells:
        data.append([cell.text.strip().encode('utf-8').decode('utf-8') for cell in cells])

# Save the scraped data to a CSV file
with open('baglung.csv', 'w',encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
