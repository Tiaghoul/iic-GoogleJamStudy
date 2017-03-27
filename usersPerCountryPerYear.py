import re
import urllib.request
import os
from bs4 import BeautifulSoup

directory = os.path.realpath(".")


def dealWithHTML(year_, lang_, html_):
    # creates new file for each lang and year
    # parses the html, gets second table,
    # and for each <a> tag, prints the country and number of contestants

    file_to_write = directory + "/usersPerCountryFiles/" + lang_ + "_" + year_ + ".csv"
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


def dealWithRedirected(year_, lang_):
    file_to_write_nothing = directory + "/usersPerCountryFiles/" + lang_ + "_" + year_ + ".csv"
    csv_file = open(file_to_write_nothing, 'w')
    print("writing NOTHING to --> " + file_to_write_nothing)

# getting all languages ever used to a list
allLanguagesFile = open("allLanguagesUsed.txt", "r")
allLangs = allLanguagesFile.readlines()
allLangs = [x.strip('\n') for x in allLangs]

# allLangs = allLangs[83:]

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]

# for every language, for every year, finds the number of contestants of each country
for lang in allLangs:
    if "/" in lang:
        lang_file = lang.replace("/", "-")
    else:
        lang_file = lang

    # deal with '#' and white spaces, but don't wanna change '+'
    if "+" not in lang:
        lang_url = urllib.parse.quote(lang)
    else:
        lang_url = lang
    print("lang_url = " + lang_url)
    for year in allYears:
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang_url
        html = urllib.request.urlopen(url)
        if url == html.geturl():
            dealWithHTML(year, lang_file, html)
        else:
            dealWithRedirected(year, lang_file)
    print("------------------------------------------------------------------------------------------")
