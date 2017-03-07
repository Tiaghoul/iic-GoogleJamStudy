import urllib.request
from bs4 import BeautifulSoup

url = "https://www.go-hero.net/jam/16/languages/C"
html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, "html.parser")

csv_file = open('idontknow.txt', 'r')
reeead = csv_file.read()
soup = BeautifulSoup(reeead, "html.parser")
tables = soup.find_all('table')
# print(tables.contents)
table = tables[1]

for e in table.findAll('br'):
    e.extract()

# print(table.contents)

for tr in table.find_all('tr'):
    print("tamanho tr = " + str(len(tr)))
    # print(tr.contents)
    tds = tr.findAll('td')
    print("num td's = " + str(len(tds)))
    # print(tds)
    # for td in tr.find_all('td'):
    #     num = td.find_all('a')
    #     print(len(num))
    #     for a in td.find_all('a'):
    #         print("---->" + a.text)
        # print(len(td))
        # print(td.text)


    # for aa in tr.find(href=True):
    #     print(len(aa))
    #     print(aa.text)
    #     next = aa.next_sibling
    #     print(next)


