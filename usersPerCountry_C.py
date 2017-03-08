import urllib.request
from bs4 import BeautifulSoup

url = "https://www.go-hero.net/jam/15/languages/C"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html5lib")

# csv_file = open('idontknow.txt', 'r')
# reeead = csv_file.read()
# soup = BeautifulSoup(reeead, "html5lib")
tables = soup.find_all('table')
# print(tables.contents)
table = tables[1]

for e in table.findAll('br'):
    e.extract()


# print(table.prettify())

for tr in table.find_all('tr'):
    print("tamanho tr = " + str(len(tr)))
    tds = tr.findAll('td')
    print("num td's = " + str(len(tds)))
    aa = tr.find_all('a')
    print(len(aa))
    for a in tr.find_all('a'):
        print(a.contents)
#
#
#         # print(td)
#         # print("-----------------------")
#     #     for a in td.find_all('a'):
#     #         print("---->" + a.text)



