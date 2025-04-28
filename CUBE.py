'''
1. A number raised to the third power is a cube. 
Plot the first five (5) cubic numbers, and 
then plot the first 5000 cubic numbers.
2. Apply a colormap to your cubes plot.
'''

import matplotlib.pyplot as plt
import matplotlib.cm as cm

x1_values = list (range(1, 6))
y1_values = [x**3 for x in x1_values]

x2_values = list (range(1, 5001))
y2_values = [x**3 for x in x2_values]

#plt.plot(x1_values, y1_values, color='green')
plt.scatter(x2_values, y2_values, c=y2_values, cmap=plt.cm.Greens, edgecolor='none', s=40)

plt.title("Cubed Ammount", fontsize=24)
plt.xlabel("Amount", fontsize=24)
plt.ylabel("Cubed Number", fontsize=24)

plt.show()