from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re 

url = input()
req = Request(url)
html_page = urlopen(req)

soup = BeautifulSoup(html_page, "lxml")

example_urls = ['https://www.facebook.com', 'https://www.linkedin.com', 'https://www.twitter.com']

links = []
for link in soup.findAll('a'):
    links.append(link.get('href'))

social_urls = []
for link in links:
    for social in example_urls:
        if social in link:
            social_urls.append(link)

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

emails = []
contacts = []

for link in links:

    if re.search(regex, link):
        emails.append(link)
    if re.search('tel:', link):
        contacts.append(link)

print("\nSocial links -")
for url in social_urls:
    print(url)

print("\nEmail/s-")
for mail in emails:
    print(mail)

print("\nContact:")
for contact in contacts:
    print(contact)