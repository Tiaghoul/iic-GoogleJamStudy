import re
import urllib.request
import os
from bs4 import BeautifulSoup

# parses the html, gets second table,
# and for each <a> tag, prints the country and number of contestants

directory = os.path.realpath(".")


def dealWithHTML(year_, lang_, html_):
    file_to_write = directory + "/usersPerCountryFiles/" + lang +  "_" + year_ + ".csv"
    csv_file = open(file_to_write, 'w')
    print("writing to --> " + file_to_write)

    soup = BeautifulSoup(html_, "html5lib", from_encoding='utf-8')
    tables = soup.find_all('table')
    table = tables[1]

    for e in table.find_all('br'):
        e.extract()

    for a in table.find_all('a'):
        country_name = a.text
        sibling = a.next_sibling
        num_contestants = re.sub("[^0-9]", "", sibling)
        csv_file.write(country_name + ", " + num_contestants + "\n")
        # print(country_name + " " + num_contestants)


# getting all languages ever used to a list
# allLanguagesFile = open("allLanguagesUsed.txt", "r")
# allLangs = allLanguagesFile.readlines()
# allLangs = [x.strip('\n') for x in allLangs]

allLangs = ['C', 'C++']

# allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
allYears = ["15", "16"]

# for every language, for every year, finds the number of contestants of each country

for lang in allLangs:
    # print("------ " + lang + " ------")
    for year in allYears:
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
        # print(url)
        html = urllib.request.urlopen(url)
        # print("Done")
        if url == html.geturl():
            print(lang + "(" + str(year) + ") --> not redirected")
            dealWithHTML(year, lang, html)
        else:
            # dealWithRedirected(...)
            print(lang + "(" + str(year) + ") --> redirected")
    print("------------------------------------------------------------------------------------------")
