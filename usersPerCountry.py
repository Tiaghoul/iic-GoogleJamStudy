import urllib.request
from bs4 import BeautifulSoup

# getting all languages ever used to a list
allLanguagesFile = open("allLanguagesUsed.txt", "r")
allLangs = allLanguagesFile.readlines()
allLangs = [x.strip('\n') for x in allLangs]

# allYears = ["08", "09", "10", "11", "12", "13", "14", "15", "16"]
allYears = ["15", "16"]

for lang in allLangs:
    for year in allYears:
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
        print(url)
        html = urllib.request.urlopen(url)
        print("Done")
        if url == html.geturl():
            print(lang + "(" + str(year) + ") --> not redirected")
        else:
            print(lang + "(" + str(year) + ") --> redirected")
    print("--------------------------------------")



# url = "https://www.go-hero.net/jam/15/languages/C"
# html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, "html5lib")
#
# tables = soup.find_all('table')
# table = tables[1]
#
# for e in table.findAll('br'):
#     e.extract()


# print(table.prettify())

# for tr in table.find_all('tr'):
#     print("tamanho tr = " + str(len(tr)))
#     tds = tr.findAll('td')
#     print("num td's = " + str(len(tds)))
#     aa = tr.find_all('a')
#     print(len(aa))
#     for a in tr.find_all('a'):
#         print(a.contents)



