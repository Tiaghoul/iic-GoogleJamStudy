import urllib.request
from bs4 import BeautifulSoup

url = "https://www.go-hero.net/jam/15/languages/C"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html5lib")

# csv_file = open('idontknow2.txt', 'w')
# reeead = csv_file.read()
# soup = BeautifulSoup(reeead, "html.parser")
print(soup.prettify())
# tables = soup.find_all('table')
# table = tables[1]

# for e in table.findAll('br'):
#     e.extract()

# a = table.find_all("tr")
# print(a.td.next_sibling)
