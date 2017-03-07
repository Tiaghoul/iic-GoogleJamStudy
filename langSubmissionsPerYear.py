import urllib.request
from bs4 import BeautifulSoup

url = "https://www.go-hero.net/jam/16/languages"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")
table = soup.table
finalWord = ""

dict = \
    {
        'Language': 0,
        'Qualification Round': 1,
        'Round 1A': 2,
        'Round 1B': 3,
        'Round 1C': 4,
        'Round 2': 5,
        'Round 3': 6,
        'Final': 7,
        'World Final': 7,
        'World Finals': 7,
        'Final Round': 7,
        'Remaining': 7,
    }



csv_file = open('jam_languages_16.csv', 'w')

first_tr = table.find_all('th')
posDict ={}
for i, hd in enumerate(first_tr):
    if hd.text in dict:
        num = dict[hd.text]
        if num == 7:
            finalWord = hd.text
        posDict[hd.text] = i


for key, num in dict.items():
    if num == 7:
        csv_file.write(finalWord)
        break
    else:
        csv_file.write(key + ", ")

csv_file.write("\n")

for tr in table.find_all('tr')[1:]:
    td = tr.find_all('td')
    if td[posDict['Language']].text != "":
        csv_file.write(td[posDict['Language']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Qualification Round']].text != "":
        csv_file.write(td[posDict['Qualification Round']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Round 1A']].text != "":
        csv_file.write(td[posDict['Round 1A']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Round 1B']].text != "":
        csv_file.write(td[posDict['Round 1B']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Round 1C']].text != "":
        csv_file.write(td[posDict['Round 1C']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Round 2']].text != "":
        csv_file.write(td[posDict['Round 2']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict['Round 3']].text != "":
        csv_file.write(td[posDict['Round 3']].text + ", ")
    else:
        csv_file.write("0, ")

    if td[posDict[finalWord]].text != "":
        csv_file.write(td[posDict[finalWord]].text)
    else:
        csv_file.write("0")

    csv_file.write("\n")

    # csv_file.write(td[posDict['Language']].text + ", " + td[posDict['Qualification Round']].text + ", " + td[posDict['Round 1A']].text + ", " + td[posDict['Round 1B']].text + ", " + td[posDict['Round 1C']].text + ", " + td[posDict['Round 2']].text + ", " + td[posDict['Round 3']].text + ", " + td[posDict[finalWord]].text + "\n");





    # for j in range(len(td)):
    #     if td[j].text == "":
    #         csv_file.write("0,-")
    #     else:
    #         csv_file.write(td[j].text + ", ")
    # csv_file.write("\n")

