import numpy as np
import operator
import matplotlib.pyplot as plt

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]


def make_the_plot(number_langs, sum_col, my_data, year_):
    list_of_tuples = []
    for i in range(number_langs):
        name_lang = my_data[i][0]
        total = 0.0

        for index, j in enumerate(my_data[i][1]):
            division = j / sum_col[index]
            total = total + division

        total = (total / 7) * 100
        list_of_tuples.append((name_lang, total))

    sorted_by_second = sorted(list_of_tuples, key=lambda tup: tup[1], reverse=True)
    first_five = sorted_by_second[:5]
    remaining_text = "Other " + str(number_langs - 5)

    five_langs = [x[0] for x in first_five]
    five_langs.append(remaining_text)

    five_percentages = [x[1] for x in first_five]
    sum_first_five = 100 - sum(x for x in five_percentages)
    five_percentages.append(sum_first_five)

    plot_values = list(range(1, 7))
    plt.xticks(plot_values, five_langs)
    plt.bar(plot_values, five_percentages)
    plt.title("Year" + year_)
    plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/best_five_each_year/best_five_' + year_ + '.png')
    plt.close()

for year in allYears:
    file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_' + year + ".csv"
    data = np.genfromtxt(file_name, comments="?", dtype=[('lang', np.str_, 50), ('values', np.int32, (7,))], skip_header=1, delimiter=',')
    sum_by_columns = np.nansum(data["values"], axis=0)
    n_langs = len(data)
    make_the_plot(n_langs, sum_by_columns, data, year)
