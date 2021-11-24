# Chomp Chomp Swamp Wikipedia URL scraper 
# development aided by BeautifulSoup documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
import requests
import re
import json
from bs4 import BeautifulSoup


# article url
articlename = input("input text file: ")
article = open(articlename, "r")
wikipedia = article.readlines()

# text file name
filename = input("output text file: ")
file = open(filename, "a")

# regex to match urls: urls can only have letters, _'s, /'s, and :'s
regex = re.compile("^[a-zA-Z/_:]*$");

i = 0

for wiki in wikipedia:
    print(str(i) + " out of " + str(len(wikipedia)))
    i+=1
    # write article url for the beginning
    file.write(wiki[:-1])

    # use requests library to get html of the article & soupify it into usable data
    page = requests.get(wiki[:-1])
    data = BeautifulSoup(page.content, "html.parser")

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
                file.write(",")
                file.write(url)

    file.write("\n")

# create new line and close CSV file
article.close()
file.close()


