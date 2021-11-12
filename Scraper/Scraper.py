# Chomp Chomp Swamp Wikipedia URL scraper 
# development aided by BeautifulSoup documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
import requests
import re
from bs4 import BeautifulSoup

# article url
article = input("Wikipedia Article URL: ")

# CSV file name
filename = input("CSV file name: ")
file = open(filename, "a")

# write article url for the beginning
file.write(article)

# use requests library to get html of the article & soupify it into usable data
page = requests.get(article)
data = BeautifulSoup(page.content, "html.parser")

# regex to match urls: urls can only have letters and /'s
regex = re.compile("^[a-zA-Z/]*$");

# general line format we want to grab from:
# <a href=URL title=TITLE>STRING</a>

# grab all the lines with the <a> (hyperlink) tag with text
for link in data.find_all('a', string=True):
    url = link.get('href')
    # filter out the urls that dont start with '/wiki/'
    if str(url).startswith("/wiki/"):
        # filter out urls that have special characters
        if (regex.match(str(url)) is not None):
            file.write(",")
            file.write(url)

# create new line and close CSV file
file.write("\n")
file.close()


