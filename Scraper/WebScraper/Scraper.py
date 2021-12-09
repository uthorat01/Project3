'''
Chomp Chomp Swamp Wikipedia URL scraper 
development aided by BeautifulSoup documentation: https://beautiful-soup-4.readthedocs.io/en/latest/
Gets all the forward links/hyper links nested on a page
Takes in a file consisting of Wikipedia articles and appends a list of hyper links on the end
'''

import requests
import re
import csv
from bs4 import BeautifulSoup

'''
Scraping
'''
# articles from text file
articlename = input("input text file: ")
article = open(articlename, "r")
wikipedia = article.readlines()

# output CSV file name
file = open("links.csv", "a")

# regex to match urls: urls can only have letters, _'s, /'s, and :'s
regex = re.compile("^[a-zA-Z/_:]*$");
print("in progress...", end='')

for wiki in wikipedia:
    # write article url for the beginning
    file.write("https://en.wikipedia.org" + wiki[:-2])

    # use requests library to get html of the article & soupify it into usable data
    page = requests.get("https://en.wikipedia.org" + wiki[:-2])
    data = BeautifulSoup(page.content, "html.parser")

    # general line format we want to grab from:
    # <a href=URL title=TITLE>STRING</a>

    # grab all the lines with the <a> (hyperlink) tag with text
    for link in data.find_all('a', string=True):
        url = link.get('href')
        # filter out the urls that dont start with '/wiki/'
        if str(url).startswith("/wiki/"):
            # we do not want any articles Help, Portal, Special, User, Wikipedia, Template, Main_Page, Template_Talk, Talk pages, or pages that are invalid (have invalid char or aren't a wiki page)
            filter = ["/wiki/Help:", "/wiki/Portal:", "/wiki/Special:", "/wiki/User:", "/wiki/Wikipedia:", "/wiki/Template:", "/wiki/Main_Page", "/wiki/Template_talk:", "/wiki/Talk:"]
            # filter out urls that have special characters aswell
            if (regex.match(str(url)) is not None and url.startswith(tuple(filter)) is not True):
                # filter out words that arent in the filter
                file.write(",")
                file.write(url)
    # go next
    file.write("\n")

# clean up
file.close()


'''
Filtering:
'''
print('filtering...', end='')

# import filter: the 'filter' consists of articles in the original inputted file
set_filter = set()
for wiki in wikipedia:
    set_filter.add(wiki[:-2])
article.close()

# export to file:
file = open("filtered.csv", "a")

# import data and filter data
with open("links.csv", newline='') as data:
    # keep track of current so that we dont want to have pages link to themselves
    current = ""
    # read in our data using a csv reader
    values = csv.reader(data, delimiter=",")
    # for each row
    for row in values:
        # for each value in the row
        for value in row:
            # if its the initial page, write it but without the beginning 
            if str(value).startswith("https"):
                current = str(value)[24:]
                file.write("\n")
                file.write(value)
                continue
            # we dont want to have pages link to themselves
            if value == current:
                continue
            # if its not a whitelisted term, delete it
            if value not in set_filter:
                continue
            # it is a whitelisted term so write it to the filtered file
            else:
                file.write(",")
                file.write(value)

# clean up
print("complete")
file.close()
data.close()


