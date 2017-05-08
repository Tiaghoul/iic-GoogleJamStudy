import numpy as np
import operator
import matplotlib.pyplot as plt

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]

five_langs = ['C', 'Java', 'Python', 'C#', 'C++']

other_langs = [100] * 8

plot_values = list(range(1, 9))
plt.xticks(plot_values, allYears)

for lang in five_langs:
    percentages = [0] * 8
    for index, one_year in enumerate(allYears):

        file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_' + one_year + '.csv'
        my_data = np.genfromtxt(file_name, comments="?", dtype=[('lang', np.str_, 16), ('values', np.int32, (7,))],
                                skip_header=1,
                                delimiter=',')

        sum_by_columns = np.nansum(my_data["values"], axis=0)

        rows = np.where(my_data['lang'] == lang)
        values_per_round = my_data[rows][0][1]
        total_percen_year = 0.0
        for index_round, val in enumerate(values_per_round):
            total_percen_year = total_percen_year + (val / sum_by_columns[index_round])
        total = (total_percen_year / 7) * 100
        percentages[index] = total
        other_langs[index] -= total

    # if lang != 'C++':
    plt.scatter(plot_values, percentages)
    plt.plot(plot_values, percentages, label=lang, linewidth=2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=6, shadow=True, title="Languages:", fancybox=True)

plt.scatter(plot_values, other_langs)
plt.plot(plot_values, other_langs, label="Other", linewidth=2)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=6, shadow=True, title="Languages:", fancybox=True)
plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/best5_evolution_years_withC++.png')
