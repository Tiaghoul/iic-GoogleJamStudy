import numpy as np
import operator
import matplotlib.pyplot as plt

x_axis_values = ['QR', 'R1A', 'R1B', 'R1C', 'R2', 'R3', 'FR']

allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
five_langs = ['C', 'Java', 'Python', 'C#', 'C++']

lang_percentage_dict = {}


def make_plot(lang, my_data):
    rows = np.where(my_data['lang'] == lang)
    sum_by_columns = np.nansum(my_data["values"], axis=0)
    values_per_round = my_data[rows][0][1]

    array_percentages = []
    for index, val in enumerate(values_per_round):
        percen = (val / sum_by_columns[index]) * 100
        array_percentages.append(percen)
        other_langs[index] -= percen
        total_percentages[index] -= percen

    # if lang != 'C++':
    plt.scatter(plot_values, array_percentages)
    plt.plot(plot_values, array_percentages, label=lang, linewidth=2)


def deal_with_year(year):
    file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/langsPerYear/langs_year_' + year + '.csv'
    data = np.genfromtxt(file_name,
                         comments="?", dtype=[('lang', np.str_, 50), ('values', np.int32, (7,))], skip_header=1,
                         delimiter=',')

    number_langs = len(data)
    for lan in five_langs:
        make_plot(lan, data)

    plt.scatter(plot_values, other_langs)
    plt.plot(plot_values, other_langs, label="Other " + str(number_langs), linewidth=2)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), shadow=True, ncol=6, title="Year 20" + year,
               fancybox=True)
    plt.savefig('/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/images/best_five_evo_per_round_withC++/best_five_evo_per_round_withC++' + year + '.png')
    plt.close()


for ano in allYears:
    plot_values = list(range(1, 8))
    plt.xticks(plot_values, x_axis_values)
    other_langs = [100] * 7
    total_percentages = [100] * 7
    deal_with_year(ano)
