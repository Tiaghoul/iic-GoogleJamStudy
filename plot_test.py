import numpy as np
import operator
import matplotlib.pyplot as plt


x_axis_values = ['QR', 'R1A', 'R1B', 'R1C', 'R2', 'R3', 'FR']

my_data = np.genfromtxt('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_16.csv', comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))], skip_header=1, delimiter=',')

sum_by_columns = np.nansum(my_data["values"], axis=0)

number_langs = len(my_data)

total_percentage = 0.0
lang_percentage_dict = {}


def makeplot(lang):
    print("LANGUAGE = " + lang)
    rows = np.where(my_data['lang'] == lang)

    values_per_round = my_data[rows][0][1]

    array_percentages = []
    for indexzinhe, val in enumerate(values_per_round):
        # print(str(val) + " " + str(sum_by_columns[indexzinhe]))
        percen = (val / sum_by_columns[indexzinhe]) * 100
        array_percentages.append(percen)

    # print(array_percentages)

    plot_values = [1, 2, 3, 4, 5, 6, 7]
    # plt.bar(plot_values, array_percentages, align='center')
    plt.xticks(plot_values, x_axis_values)

    plt.scatter(plot_values, array_percentages)
    plt.plot(plot_values, array_percentages, label=lang, linewidth=2)
    plt.legend(loc='upper left', shadow=True, ncol=2, title="Languages:", fancybox=True)


for lan in ["Java", "C++"]:
    makeplot(lan)

plt.show()

# plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/java_16.png')