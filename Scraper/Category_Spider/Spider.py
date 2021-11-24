# requests each category, gets all forward links on category, and does the same for each category found on it

import requests
import re
import json
from bs4 import BeautifulSoup

filename = input("CSV file name: ")
file = open(filename, "r")

filename = input("SECOND CSV file name: ")
secondfile = open(filename, "a")

filelines = file.readlines()

regex = re.compile("^[a-zA-Z/_:]*$")
i = 0

for line in filelines:
    print(str(i) + " out of " + str(len(filelines)))
    i+=1
    if str(line).startswith("/wiki/Category:"):
        temp = False
        filterfile = open('filter.json', "r+")
        filt = json.load(filterfile)
        article = "https://en.wikipedia.org/" + str(line)
        page = requests.get(article[:-2])
        data = BeautifulSoup(page.content, "html.parser")
        for link in data.find_all('a'):
            url = link.get("href")
            if str(url).startswith("/wiki/Help") or str(url).startswith("/wiki/Portal:") or str(url).startswith("/wiki/Special:") or str(url).startswith("/wiki/Wikipedia:") or str(url).startswith("/wiki/Main_Page") or str(url).startswith("/wiki/Template:"):
                continue
            if str(url).startswith("/wiki/"):
                for keyword in filt['filter']:
                    if str(keyword).startswith(str(url)):
                        temp = True
                        break
                if temp is True:
                    continue
                filt['filter'].append(str(line))
                filterfile.seek(0)
                filterfile.write(json.dumps(filt))
                filterfile.truncate()
                if regex.match(str(url)) is not None:
                    secondfile.write(str(url))
                    secondfile.write(",\n")
        filterfile.close()
    else:
        secondfile.write(line)

file.close()
secondfile.close()