#!/usr/bin/python3

import numpy as np
import os

directory = os.path.realpath(".")


allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
# allYears = ["16"]


all_countries_file = open("../allCountries.txt")
all_countries = all_countries_file.readlines()
all_countries = [x.strip('\n') for x in all_countries]

tuples_list = []

for country in all_countries:
    percentages = [0] * 8
    total_percentage = 0
    for index, one_year in enumerate(allYears):
        file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/usersPerYear/users_year_' + one_year + '.csv'
        my_data = np.genfromtxt(file_name, comments="?", dtype=[('country', np.str_, 50), ('values', np.int32, (7,))],
                                skip_header=1,
                                delimiter=',')

        sum_by_columns = np.nansum(my_data["values"], axis=0)

        rows = np.where(my_data['country'] == str(country))
        if len(rows[0]) > 0:
            values_per_round = my_data[rows][0][1]
            total_percen_year = 0.0
            for index_round, val in enumerate(values_per_round):
                total_percen_year += (val / sum_by_columns[index_round])
            tmp = (total_percen_year / 7) * 100
            total_percentage += tmp
    tuples_list.append((country, total_percentage / 8))

sorted_by_second = sorted(tuples_list, key=lambda tup: tup[1], reverse=True)
# print(sorted_by_second)

file_to_write = directory + "/../allCountriesPercentages.csv"
csv_file = open(file_to_write, 'w')

# print(file_to_write)
for (x,y) in sorted_by_second:
    csv_file.write(x + ", " + str(y) + "\n")
csv_file.close()
