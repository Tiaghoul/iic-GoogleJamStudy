import numpy as np
import operator
import matplotlib.pyplot as plt

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]

all_languages_file = open("allLanguagesUsedPercentages.csv")
all_langs_tmp = all_languages_file.readlines()


def make_plot(all_langs, n):
    for lang in all_langs:
        percentages = [0] * 8
        for index, one_year in enumerate(allYears):
            file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_' + one_year + '.csv'
            my_data = np.genfromtxt(file_name, comments="?", dtype=[('lang', np.str_, 50), ('values', np.int32, (7,))],
                                    skip_header=1,
                                    delimiter=',')

            sum_by_columns = np.nansum(my_data["values"], axis=0)

            rows = np.where(my_data['lang'] == lang)
            if len(rows[0]) > 0:
                values_per_round = my_data[rows][0][1]
                total_percen_year = 0.0
                for index_round, val in enumerate(values_per_round):
                    total_percen_year = total_percen_year + (val / sum_by_columns[index_round])
                total = (total_percen_year / 7) * 100
                percentages[index] = total
            else:
                percentages[index] = 0

        plot_values = list(range(1, 9))
        plt.xticks(plot_values, allYears)
        plt.scatter(plot_values, percentages)
        plt.plot(plot_values, percentages, label=lang, linewidth=2)
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=8, shadow=True, title="Languages:", fancybox=True)

    file_name = str(n+1) + "_to_" + str(n+5) + "_evo_per_year"
    plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/6_to_20/' + file_name + '.png')
    plt.close()

for i in [5, 10, 15]:
    all_langs_ = [x.split(',')[0] for x in all_langs_tmp][i:i+5]
    make_plot(all_langs_, i)
