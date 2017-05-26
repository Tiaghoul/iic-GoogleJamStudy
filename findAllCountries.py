import urllib.request
from bs4 import BeautifulSoup

txt_file = open('allCountries.txt', 'w')
anos = ["09", "10", "11", "12", "13", "14", "15", "16"]
allCountries = []

for ano in anos:
    url = "https://www.go-hero.net/jam/" + ano + "/regions"
    print("New request: " + url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.table

    for tr in table.find_all('tr')[1:]:
        lang = tr.td.text
        if lang not in allCountries:
            allCountries.append(lang)


allCountries.sort()

for l in allCountries[1:]:
    txt_file.write(l + "\n")
