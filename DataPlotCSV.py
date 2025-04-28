import csv

filename = 'earthquakes24hrs-04232025.csv'

# print column headers
with open(filename, encoding="utf8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

#    for index, column_header in enumerate(header_row):
#        print(index, column_header)

    mag = []
    for row in reader:
        mag_f = float(row[8])
        mag.append(mag_f)
#        print(mag)

from matplotlib import pyplot as plt

# plot data
fig = plt.figure(dpi=96, figsize = (10,6))
plt.plot(mag, c='red')

# format plot
plt.title('Earthquakes in 24 hours', fontsize= 24)
plt.xlabel('Number of', fontsize = 16)
plt.ylabel('Magnitude', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()