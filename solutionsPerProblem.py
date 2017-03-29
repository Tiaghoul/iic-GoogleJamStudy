import urllib.request
import os
from bs4 import BeautifulSoup

dictionary = {
        'Qualification Round': 'QR',
        'Round 1A': 'R1A',
        'Round 1B': 'R1B',
        'Round 1C': 'R1C',
        'Round 2': 'R2',
        'Round 3': 'R3',
        'Final': 'FR',
        'World Final': 'FR',
        'World Finals': 'FR',
        'Final Round': 'FR',
        'Remaining': 'FR',
}

directory = os.path.realpath(".") + "/setsPerProblem/"

# existem problemas que não tem "large sets".. fica a 0??
# existem problemas que tem "large-1" sets e "large-2" sets, adiciono os 2?


def writeSetsToFile(year_, lang_, dt_tags):
    for dt_tag in dt_tags:
        dt_b_tag = dt_tag.b.get_text()
        dict_value = dictionary[dt_b_tag]
        dd_tag = dt_tag.next_sibling
        dd_ul_tag = dd_tag.ul

        for li in dd_ul_tag.find_all('li'):
            problem_name = li.a.get_text()
            problem_name = problem_name.replace(" ", "")
            file_name = year_ + "_" + dict_value + "_" + problem_name + ".csv"
            file_to_write = open(directory + file_name, 'a')

            list_of_words = li.get_text().split()

            if "small" in list_of_words:
                small_value = list_of_words[list_of_words.index("small") - 1]
            else:
                small_value = "0"
            if "large" in list_of_words:
                large_value = list_of_words[list_of_words.index("large") - 1]
            elif "large-1" in list_of_words and "large-2" in list_of_words:
                # value = max(int(list_of_words[list_of_words.index("large-1") - 1]), int(list_of_words[list_of_words.index("large-2") - 1]))
                value = int(list_of_words[list_of_words.index("large-1") - 1]) + int(
                    list_of_words[list_of_words.index("large-2") - 1])
                large_value = str(value)
            elif "large-1" in list_of_words:
                value = list_of_words[list_of_words.index("large-1") - 1]
                large_value = str(value)
            elif "large-2" in list_of_words:
                value = list_of_words[list_of_words.index("large-2") - 1]
                large_value = str(value)
            else:
                large_value = "0"
            file_to_write.write(lang_ + ", " + small_value + ", " + large_value + "\n")
            file_to_write.close()
            print(lang_ + ", " + small_value + ", " + large_value)

# allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
all_years = ["13", "15"]

# getting all languages ever used to a list
# allLanguagesFile = open("allLanguagesUsed.txt", "r")
# all_langs = allLanguagesFile.readlines()
# all_langs = [x.strip('\n') for x in allLangs]
all_langs = ["C++", "AutoIt"]

lang_url = ""

for year in all_years:
    for lang in all_langs:
        if "+" not in lang:
            lang_url = urllib.parse.quote(lang)
        else:
            lang_url = lang
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
        print("Request for: " + url)
        html = urllib.request.urlopen(url)
        print("Request for " + url + " is done!")
        if url == html.geturl():
            soup = BeautifulSoup(html, 'html5lib', from_encoding='utf-8')
            dl_tag = soup.dl
            all_dt_tags = dl_tag.find_all('dt')
            writeSetsToFile(year, lang, all_dt_tags)
        else:
            print("lang " + lang + " not used in year " + year)
        print("----------------------------------------------")
