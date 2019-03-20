import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
y = []

# Reading data from txt using csv 
with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots: 
        x.append(int(row[0]))
        y.append(int(row[1]))


# From Numpy

w = []
z = []



plt.plot(x,y, label="loaded from file")


plt.xlabel('x')
plt.ylabel('y')
plt.title('title')
plt.legend()
plt.show()













