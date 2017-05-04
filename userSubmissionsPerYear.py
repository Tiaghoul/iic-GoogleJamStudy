import urllib.request
import os
from bs4 import BeautifulSoup


finalWord = ""
directory = os.path.realpath(".")
allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]

dictionary = {
        'Country': 0,
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

for year in allYears:
    fileToWrite = directory + "/usersPerYear/users_year_" + year + ".csv"
    csv_file = open(fileToWrite, 'w')
    print("writing to --> " + fileToWrite)

    url = "https://www.go-hero.net/jam/" + year + "/regions"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.table

    first_tr = table.find_all('th')
    print(first_tr)
    posDict = {}
    for i, hd in enumerate(first_tr):
        if hd.text in dictionary:
            num = dictionary[hd.text]
            if num == 7:
                finalWord = hd.text
            posDict[hd.text] = i
        else:
            print(hd.text + "not in dictionary")

    for key, num in dictionary.items():
        if num == 7:
            csv_file.write(finalWord)
            break
        else:
            csv_file.write(key + ", ")

    csv_file.write("\n")

    for tr in table.find_all('tr')[1:]:
        td = tr.find_all('td')
        if td[posDict['Country']].text != "":
            csv_file.write(td[posDict['Country']].text + ", ")
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
