import urllib.request
from bs4 import BeautifulSoup

txt_file = open('allLanguagesUsed.txt', 'w')
anos = ["09", "10", "11", "12", "13", "14", "15", "16"]
allLanguages = []

for ano in anos:
    url = "https://www.go-hero.net/jam/" + ano + "/languages"
    print("New request: " + url)
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.table

    for tr in table.find_all('tr')[1:]:
        lang = tr.td.text
        if lang not in allLanguages:
            allLanguages.append(lang)


allLanguages.sort()

for l in allLanguages:
    txt_file.write(l + "\n")
