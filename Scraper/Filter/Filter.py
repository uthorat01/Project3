import json
import csv

# import filter
filterfile = open("filter.json", "r")
filter = json.load(filterfile)
set_filter = set(filter['filter'])

# export to file:
file = open("filtered.csv", "a")

# import data and filter data
with open("links.csv", newline='') as data:
    i=0
    current = ""
    values = csv.reader(data, delimiter=",")
    for row in values:
        print(str(i) + " out of 71920")
        i+=1
        for value in row:
            if str(value).startswith("https"):
                current = str(value)[24:]
                file.write("\n")
                file.write(value)
                continue
            if value == current:
                continue
            if value not in set_filter:
                continue
            else:
                file.write(",")
                file.write(value)

# clean up
filterfile.close()
file.close()
data.close()
