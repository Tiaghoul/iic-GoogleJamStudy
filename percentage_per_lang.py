import numpy as np
import pprint
import operator
from itertools import islice
import matplotlib.pyplot as plt


def take(n, iterable):
    return list(islice(iterable, n))

x_axis_values = ['QR', 'R1A', 'R1B', 'R1C', 'R2', 'R3', 'FR']

my_data = np.genfromtxt('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_16.csv', comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))], skip_header=1, delimiter=',')

sum_by_columns = np.nansum(my_data["values"], axis=0)

print(sum_by_columns)

number_langs = len(my_data)
print(number_langs)

total_percentage = 0.0
lang_percentage_dict = {}
#
# rows = np.where(my_data['lang'] == 'Java')
#
# values_per_round = my_data[rows][0][1]
#
# array_percentages = []
# for indexzinhe, val in enumerate(values_per_round):
#     # print(str(val) + " " + str(sum_by_columns[indexzinhe]))
#     percen = (val/sum_by_columns[indexzinhe])*100
#     array_percentages.append(percen)
#
# # print(array_percentages)
#
# plot_values = [1,2,3,4,5,6,7]
# plt.bar(plot_values, array_percentages, align='center')
# plt.xticks(plot_values, x_axis_values)
# plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/java_16.png')

# add to list of tuples instead of dict

for i in range(number_langs):
    # print(my_data[i][1])
    name_lang = my_data[i][0]
    # print(name_lang)
    total = 0.0
    for index, j in enumerate(my_data[i][1]):
        # print(j)
        # print(sum_by_columns[index])
        division = j/sum_by_columns[index]
        # print("division " + str(index) + " = " + str(division))
        total = total + division
        # print("---------")
    # print("total antes = " + str(total))
    total = (total/7) * 100
    total_percentage += total
    lang_percentage_dict[name_lang] = total
    # print("percentagem = " + str(total))
    # print("-------------------------------------")

# print(lang_percentage_dict)

sorted_value = sorted(lang_percentage_dict.items(), key=operator.itemgetter(1), reverse=True)
twenty_langs = list(zip(*sorted_value))[0]
twenty_percentages = list(zip(*sorted_value))[1]

print(twenty_langs)

# pprint.pprint(sorted_value)
# print("total percentage = " + str(total_percentage))
# print(lang_percentage_dict)
# twenty_first = take(20, sorted_value.iteritems())
# pprint.pprint(twenty_first)





