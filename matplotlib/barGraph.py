import matplotlib.pyplot as plt


""" Bar chart
# dataset 1
x = [2,4,6,8,10]
y = [6,7,8,2,4]

# dataset 2
x2 = [1,3,5,8]
y2 = [8,5,6,7]

# plotting as bar graph
plt.bar(x, y, label="Bars1", color='r')
plt.bar(x2,y2, label="Bars2", color='c') """


# histograms, which are used to show distribution

# dataset 1
population_ages = [22, 55, 63, 21,23,29,29,29,29,29,29,29,29,22, 55, 100, 120, 40, 49, 34, 56,76,70]
# enhanced for loop to populate ids
# ids = [x for x in range(len(population_ages))]

bins = [0, 10, 20, 30, 40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

msg = 'hi'


plt.xlabel('plot number')
plt.ylabel('Important var')

plt.title('Interesting graph..\ncheck it out')

plt.legend()
plt.show()