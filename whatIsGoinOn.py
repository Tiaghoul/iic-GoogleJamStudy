import urllib.request
from bs4 import BeautifulSoup



url = "https://www.go-hero.net/jam/15/languages/C"
html = urllib.request.urlopen(url)

urlUsed = html.geturl()

file = open("/home/tiaghoul/PycharmProjects/IIC_project/usersPerCountryFiles/gottem1.txt", "a")

if url == urlUsed:
    file.write("not redirected\n")
else:
    file.write("redirected\n")



# a = table.find_all("tr")
# print(a.td.next_sibling)
