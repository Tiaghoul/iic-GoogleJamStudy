import numpy as np
import operator
import matplotlib.pyplot as plt


x_axis_values = ['QR', 'R1A', 'R1B', 'R1C', 'R2', 'R3', 'FR']

my_data = np.genfromtxt('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_16.csv', comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))], skip_header=1, delimiter=',')

sum_by_columns = np.nansum(my_data["values"], axis=0)

print(sum_by_columns)

number_langs = len(my_data)
print(number_langs)

total_percentage = 0.0

list_of_tuples = []

# add to list of tuples instead of dict

for i in range(number_langs):
    name_lang = my_data[i][0]
    total = 0.0

    for index, j in enumerate(my_data[i][1]):
        division = j/sum_by_columns[index]
        total = total + division

    total = (total/7) * 100
    total_percentage += total
    list_of_tuples.append((name_lang, total))

sorted_by_second = sorted(list_of_tuples, key=lambda tup: tup[1], reverse=True)
first_five = sorted_by_second[:5]

remaining_text = "Other " + str(number_langs-5)

five_langs = [x[0] for x in first_five]
five_langs.append(remaining_text)

five_percentages = [x[1] for x in first_five]
sum_first_five = 100 - sum(x for x in five_percentages)
five_percentages.append(sum_first_five)

plot_values = list(range(1, 7))
plt.xticks(plot_values, five_langs)
plt.bar(plot_values, five_percentages)
plt.show()





