import urllib.request
from bs4 import BeautifulSoup

def dealWithHTML(year, lang, html):
    soup = BeautifulSoup(html, "html5lib", fromEncoding='utf-8')
    tables = soup.find_all('table')
    table = tables[1]

    for e in table.find_all('br'):
        e.extract()

    # print(table.prettify())

    for a in table.find_all('a'):
        countryName = a.text
        print(countryName)



# getting all languages ever used to a list
# allLanguagesFile = open("allLanguagesUsed.txt", "r")
# allLangs = allLanguagesFile.readlines()
# allLangs = [x.strip('\n') for x in allLangs]

allLangs = ['C', 'C++']

# allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
allYears = ["15", "16"]

#for every language, for every year, finds the number of contestants of each country
for lang in allLangs:
    # print("------ " + lang + " ------")
    for year in allYears:
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
        print(url)
        html = urllib.request.urlopen(url)
        print("Done")
        if url == html.geturl():
            print(lang + "(" + str(year) + ") --> not redirected")
            dealWithHTML(year, lang, html)
        else:
            #todo
            # dealWithRedirected(...)
            print(lang + "(" + str(year) + ") --> redirected")
    print("------------------------------------------------------------------------------------------")


# for tr in table.find_all('tr'):
#     print("tamanho tr = " + str(len(tr)))
#     tds = tr.findAll('td')
#     print("num td's = " + str(len(tds)))
#     aa = tr.find_all('a')
#     print(len(aa))
#     for a in tr.find_all('a'):
#         print(a.contents)



