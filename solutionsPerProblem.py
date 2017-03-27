import urllib.request
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

# existem problemas que não tem "large sets".. fica a 0??
# existem problemas que tem "large-1" sets e "large-2" sets, adiciono os 2?


def writeSetsToFile(year_, lang_, dt_tags):
    for dt in dt_tags:
        dt_b = dt.b.get_text()
        print(dt_b)
        dict_value = dictionary[dt_b]
        dd_in_dt = dt.next_sibling
        dd_ul = dd_in_dt.ul

        for li in dd_ul.find_all('li'):
            problem_name = li.a.get_text()
            file_name = year_ + "_" + dict_value + "_" + problem_name + ".csv"
            print(file_name)
            # print(problem_name)
            text = li.get_text()
            list_of_words = text.split()

            small_value = ""
            large_value = ""

            if "small" in list_of_words:
                small_value = list_of_words[list_of_words.index("small") - 1]
            else:
                small_value = "0"
            if "large" in list_of_words:
                large_value = list_of_words[list_of_words.index("large") - 1]
            elif "large-1" in list_of_words and "large-2" in list_of_words:
                value = int(list_of_words[list_of_words.index("large-1") - 1]) + int(
                    list_of_words[list_of_words.index("large-2") - 1])
                large_value = str(value) + "!!"
            else:
                large_value = "0"
            print(lang_ + ", " + small_value + ", " + large_value + "\n")


# allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
all_years = ["15"]

# getting all languages ever used to a list
# allLanguagesFile = open("allLanguagesUsed.txt", "r")
# all_langs = allLanguagesFile.readlines()
# all_langs = [x.strip('\n') for x in allLangs]
all_langs = ["C++", "deez", "Kotlin"]

lang_url = ""

for year in all_years:
    for lang in all_langs:
        if "+" not in lang:
            lang_url = urllib.parse.quote(lang)
        else:
            lang_url = lang
        url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
        html = urllib.request.urlopen(url)
        if url == html.geturl():
            soup = BeautifulSoup(html, 'html5lib')
            dl_tag = soup.dl
            all_dt_tags = dl_tag.find_all('dt')
            writeSetsToFile(year, lang, all_dt_tags)
        else:
            # dealWithRedirected(year, lang_file)
            print("lang " + lang + " not used in year " + year)
        print("----------------------------------------------")