# Chomp Chomp Swamp Wikipedia URL scraper 
# development aided by BeautifulSoup documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
import requests
import re
import json
from bs4 import BeautifulSoup

# article url
article = input("Wikipedia Article URL: ")

# CSV file name
filename = input("CSV file name: ")
file = open(filename, "a")

# JSON filter
filterfile = open('filter.json',)
filter = json.load(filterfile)

# write article url for the beginning
file.write(article)

# use requests library to get html of the article & soupify it into usable data
page = requests.get(article)
data = BeautifulSoup(page.content, "html.parser")

# regex to match urls: urls can only have letters, _'s, and /'s
regex = re.compile("^[a-zA-Z/_]*$");

# general line format we want to grab from:
# <a href=URL title=TITLE>STRING</a>

# grab all the lines with the <a> (hyperlink) tag with text
for link in data.find_all('a', string=True):
    url = link.get('href')
    # filter out the urls that dont start with '/wiki/'
    if str(url).startswith("/wiki/"):
        # filter out urls that have special characters
        if (regex.match(str(url)) is not None):
            # filter out words that arent in the filter
            for keyword in filter['filter']:
                if str(url).endswith(keyword):
                    file.write(",")
                    file.write(url)

# create new line and close CSV file
file.write("\n")
file.close()
filterfile.close()


