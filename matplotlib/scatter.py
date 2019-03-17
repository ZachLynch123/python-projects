import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [3,4,5,7,7,8,4,6]

plt.scatter(x,y, label='scatter', color='k')


plt.xlabel('x')
plt.ylabel('y')


plt.title("scatter plot")
plt.legend()
plt.show()







