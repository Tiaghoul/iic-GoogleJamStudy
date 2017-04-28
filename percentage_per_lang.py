import numpy as np
import pprint
import operator
import matplotlib.pyplot as plt


my_data = np.genfromtxt('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_11.csv', comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))], skip_header=1, delimiter=',')

sum_by_columns = np.nansum(my_data["values"], axis=0)

print(sum_by_columns)

number_langs = len(my_data)

total_percentage = 0.0
lang_percentage_dict = {}

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

sorted_value = sorted(lang_percentage_dict.items(), key=operator.itemgetter(1), reverse=True)
pprint.pprint(sorted_value)
print("total percentage = " + str(total_percentage))
# print(lang_percentage_dict)




