import numpy as np
import operator
import matplotlib.pyplot as plt


allYears = ["09", "10", "11", "12", "13", "14", "15", "16"]
# allYears = ["14","15"]

dict_times = {}
dict_participants = {}

for year in allYears:
    print(year)
    file_name = '/home/tiaghoul/PycharmProjects/iic-GoogleJamStudy/usersPerYear/users_year_' + year + '.csv'
    print(file_name)

    my_data = np.genfromtxt(file_name, comments="?", dtype=None, skip_header=1, delimiter=',',)

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


sorted_times = sorted(dict_times.items(), key=operator.itemgetter(1), reverse=True)
sorted_participants = sorted(dict_participants.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_times)
print(sorted_participants)

list_countries_times = [x[0] for x in sorted_times]
listzinhe = [(x,dict_participants[x]/dict_times[x]) for x in list_countries_times]

sorted_media = sorted(listzinhe, key=operator.itemgetter(1), reverse=True)

print(listzinhe)
print(sorted_media)
# list_times = [x[1] for x in sorted_times]
# list_countries_part = [x[0] for x in sorted_participants]
# list_part = [x[1] for x in sorted_participants]

# print(len(list_countries_times))
# plot_values = list(range(1, len(list_countries_times)+1))
# plt.xticks(plot_values, list_countries_times,  rotation='vertical')
# plt.bar(plot_values, list_times)
# plt.show()

