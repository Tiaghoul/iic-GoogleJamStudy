import re
from urllib import request, parse
import os
from bs4 import BeautifulSoup

directory = os.path.realpath(".")

# getting all languages ever used to a list
all_languages_file = open("allLanguagesUsed.txt", "r")
all_langs = all_languages_file.readlines()
all_langs = [x.strip('\n') for x in all_langs]

all_years = ["09", "10", "11", "12", "13", "14", "15", "16"]


def deal_with_HTML(year_, lang_, html_):
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

    csv_file.close()


def deal_with_redirected(year_, lang_):
    # when a language is not used in a specific year, creates a blank file
    file_to_write_nothing = directory + "/usersPerCountryFiles/" + lang_ + "_" + year_ + ".csv"
    csv_file = open(file_to_write_nothing, 'w')
    print("writing NOTHING to --> " + file_to_write_nothing)


# for every language, for every year, finds the number of contestants of each country
for lang in all_langs:
    if "/" in lang:
        lang_file = lang.replace("/", "-")
    else:
        lang_file = lang

    # deal with '#' and white spaces, but don't wanna change '+'
    if "+" not in lang:
        lang_url = parse.quote(lang)
    else:
        lang_url = lang
    print("lang_url = " + lang_url)
    for year in all_years:
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang_url
        html = request.urlopen(url)
        if url == html.geturl():
            deal_with_HTML(year, lang_file, html)
        else:
            deal_with_redirected(year, lang_file)
    print("------------------------------------------------------------------------------------------")
