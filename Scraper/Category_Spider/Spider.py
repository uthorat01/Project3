'''
Wikipedia 'Spider' Program:
    Starts at an initial category,
    Gets all pages stemming from the initial category whose parent page is a category.
    No repeats.
'''

import requests
import re
from bs4 import BeautifulSoup

# get initial data
initialcat = input("Initial Category (https://en.wikipedia.org/wiki/Category:...): ")
datapoints = input("Desired # of Data Points: ")

# get output file (.CSV or .TXT recommended)
outputfile = input("Output file path: ")

# format & prevent duplicates
regex = re.compile("^[a-zA-Z/_:]*$")
set_filter = set()
queue = []

# start scraping: add to output file & add inital cat to queue
print('in progress...', end='')
queue.append(initialcat)

# while queue is not empty
while queue and len(set_filter) < int(datapoints):
    # pop page from queue
    page = queue.pop()
    # if page is a category:
    if "/wiki/Category:" in page:
        # first, make it a full url
        if page.startswith("https") is False:
            page = "https://en.wikipedia.org" + page
        # get all the hyperlinks nested on the page using BS4
        article = requests.get(page)
        html = BeautifulSoup(article.content, "html.parser")
        for link in html.find_all('a'):
            url = str(link.get('href'))
            # we do not want any articles Help, Portal, Special, User, Wikipedia, Template, Main_Page, Template_Talk, Talk pages, or pages that are invalid (have invalid char or aren't a wiki page)
            filter = ["/wiki/Help:", "/wiki/Portal:", "/wiki/Special:", "/wiki/User:", "/wiki/Wikipedia:", "/wiki/Template:", "/wiki/Main_Page", "/wiki/Template_talk:", "/wiki/Talk:"]
            if url.startswith("/wiki/") is False or url.startswith(tuple(filter)) or regex.match(url) is None:
                continue
            # add to set and queue unless it has already been added to set_filter
            if url.startswith("/wiki/Category:") and url not in set_filter:
                queue.append(url)
            set_filter.add(url)

# write set_filter to output file
file = open(outputfile, "a")
for page in set_filter:
    file.write("https://en.wikipedia.org")
    file.write(page)
    file.write(",\n")

# clean up
print("complete")
set_filter.clear()
queue.clear()
file.close()