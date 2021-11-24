# fetches all the category type links from a CSV

import json

filename = input("CSV file name: ")
file = open(filename, "r")

secondfile = open("cats.txt", "a")

lines = file.readlines()

for line in lines:
    if str(line).startswith("/wiki/Category"):
        secondfile.write(line)

file.close()
secondfile.close()


