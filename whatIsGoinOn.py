import urllib.request
from bs4 import BeautifulSoup
import pprint

url = "https://www.go-hero.net/jam/15/languages/C"
html = urllib.request.urlopen(url)
# soup = BeautifulSoup(html, "html.parser")

csv_file = open('idontknow.txt', 'r')
reeead = csv_file.read()
soup = BeautifulSoup(reeead, "html.parser")
print(soup.prettify())
# tables = soup.find_all('table')
# table = tables[1]

# for e in table.findAll('br'):
#     e.extract()

# a = table.find_all("tr")
# print(a.td.next_sibling)
# pp = pprint.PrettyPrinter(indent=2)
# pp.pprint(a)