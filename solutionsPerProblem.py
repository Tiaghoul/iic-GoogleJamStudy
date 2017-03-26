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
small_value = "3"
large_value = "5"

year = "15"
lang = "C++"
url = "https://www.go-hero.net/jam/" + year + "/languages/" + lang
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html5lib')

dl_tag = soup.dl

all_dt_tags = dl_tag.find_all('dt')
# print(len(dl_tag))
# print(len(all_dt_tags))

# existem problemas que não tem "large sets".. fica a 0??
# existem problemas que tem "large-1" sets e "large-2" sets, adiciono os 2?

for dt in all_dt_tags:
    dt_b = dt.b.get_text()
    print(dt_b)
    dict_value = dictionary[dt_b]
    dd_in_dt = dt.next_sibling
    dd_ul = dd_in_dt.ul

    for index, li in enumerate(dd_ul.find_all('li')):
        file_name = year + "_" + dict_value + "_"  + str(index+1) + ".csv"
        print(file_name)

        text = li.get_text()
        list_of_words = text.split()

        if "small" in list_of_words:
            small_value = list_of_words[list_of_words.index("small") - 1]
        else:
            small_value = "0"
        if "large" in list_of_words:
            large_value = list_of_words[list_of_words.index("large") - 1]
        elif "large-1" in list_of_words and "large-2" in list_of_words:
            value = int(list_of_words[list_of_words.index("large-1") - 1]) + int(list_of_words[list_of_words.index("large-2") - 1])
            large_value = str(value) + "!!"
        else:
            large_value = "0"
        print(lang + ", " + small_value + ", " + large_value + "\n")
