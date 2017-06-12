import numpy as np
import operator
import os

directory = os.path.realpath(".")
file_to_write = directory + "/analyses/countries_in_finals.csv"


allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]

dict_times = {}
dict_participants = {}

for year in allYears:
    file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/usersPerYear/users_year_' + year + '.csv'

    my_data = np.genfromtxt(file_name, comments="?", dtype=None, skip_header=1, delimiter=',')

    for row in my_data:
        # print(row)
        if row[7] > 0:
            country = row[0].decode('UTF-8')
            n_users = int(row[7])
            if country in dict_times:
                dict_times[country] += 1
            else:
                dict_times[country] = 1
            if country in dict_participants:
                dict_participants[country] += n_users
            else:
                dict_participants[country] = n_users

# escrever cada uma destas listas para um ficheiro
sorted_times = sorted(dict_times.items(), key=operator.itemgetter(1), reverse=True)[:7]
sorted_participants = sorted(dict_participants.items(), key=operator.itemgetter(1), reverse=True)[:7]

sorted_by_c_times = sorted(sorted_times, key=operator.itemgetter(0))
sorted_by_c_participants = sorted(sorted_participants, key=operator.itemgetter(0))

all_times = [x[1] for x in sorted_by_c_times]
all_participants = [x[1] for x in sorted_by_c_participants]
all_countries = [x[0] for x in sorted_by_c_participants]


csv_file = open(file_to_write, 'w')
for i in range(7):
    print(all_countries[i] + " " + str(all_times[i]) + " " + str(all_participants[i]))
    csv_file.write(all_countries[i] + " " + str(all_times[i]) + " " + str(all_participants[i]) + "\n")

csv_file.close()

# N = 7
# ind = np.arange(N)
# width = 0.27

# plot_values = list(range(1, len(all_countries)+1))
# plt.xticks(ind+width, all_countries, rotation='vertical')
# plt.bar(ind, all_times, width)
# plt.bar(ind+width, all_participants, width)
# plt.ylabel('Best 7 countries')
# plt.show()

