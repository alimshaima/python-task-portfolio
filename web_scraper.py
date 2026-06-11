# Web Scraper (BeautifulSoup)
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

quotes = soup.find_all('span', class_='text')
print("Top 5 quotes:\n")

for i, quote in enumerate(quotes[:5], 1):
    print(f"{i}. {quote.get_text()}")
