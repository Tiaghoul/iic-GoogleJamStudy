import numpy as np
import operator
import matplotlib.pyplot as plt

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
# allYears = ["10", "12"]

# all_languages_file = open("allLanguagesUsed.txt")
# all_langs = all_languages_file.readlines()
# all_langs = [x.strip('\n') for x in all_langs]
all_langs = ['C', 'Ruby']

plot_values = list(range(1, 9))
plt.xticks(plot_values, allYears)

tuples_list = []

for lang in all_langs:
    percentages = [0] * 8
    total_percentage = 0
    for index, one_year in enumerate(allYears):
        print(one_year)
        file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_' + one_year + '.csv'
        my_data = np.genfromtxt(file_name, comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))],
                                skip_header=1,
                                delimiter=',')

        sum_by_columns = np.nansum(my_data["values"], axis=0)

        rows = np.where(my_data['lang'] == lang)
        if len(rows[0]) > 0:
            values_per_round = my_data[rows][0][1]
            total_percen_year = 0.0
            for index_round, val in enumerate(values_per_round):
                total_percen_year += (val / sum_by_columns[index_round])
            tmp = (total_percen_year / 7) * 100
            total_percentage += tmp

    tuples_list.append((lang, total_percentage))
    # print("---------------------------------------")

print(tuples_list)
# sorted_by_second = sorted(tuples_list, key=lambda tup: tup[1], reverse=True)
# print(sorted_by_second)
