from urllib import request
import os
from bs4 import BeautifulSoup

directory = os.path.realpath(".") + "/multiLangs/"
all_years = ["09", "10", "11", "12", "13", "14", "15", "16"]

file_more_langs = open(directory + "more_langs_used.csv", 'w')
file_num_contestants = open(directory + "contestants_multiple_langs.csv", 'w')


def main_function(year):
    url = "https://www.go-hero.net/jam/" + year + "/multilang"
    html = request.urlopen(url)
    soup = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')

    tbody = soup.table.tbody
    all_trs = tbody.find_all('tr')[1:]
    number_contestants = len(all_trs)
    first_contestant = all_trs[0].contents[1].get_text()

    full_year = "20" + year
    file_more_langs.write(full_year + ", " + str(first_contestant) + "\n")
    file_num_contestants.write(full_year + ", " + str(number_contestants) + "\n")
    print(number_contestants)
    print(first_contestant)

for y in all_years:
    main_function(y)
