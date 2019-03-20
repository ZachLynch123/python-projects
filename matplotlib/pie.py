import matplotlib.pyplot as plt 

days = [1,2,3,4,5]

sleeping = 7
eating = 2
working = 7
playing = 8

slices = [7,2,7,8]
activities = ['sleeping', 'eating', 'working', 'playing']
color = ['c','m','k', 'r']

# Can set starting angle
# Can also 'pull out' a piece of the pie with explode()
# add percentages using autopct and some regex

plt.pie(slices,
labels=activities,
colors=color,
startangle=90, 
explode=(0,0.1,0,0),
autopct='%1.1f%%')

plt.show()















