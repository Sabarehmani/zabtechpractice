import matplotlib.pyplot as plt
categories = ['A' ,'B','C','D','E','F','G','H']
values = [2,3,4,5,6,7,8,9,15]
plt.xlabel('categories')
plt.ylabel('values')
plt.bar(categories,values,color='red',linewidth=2,edgecolor='black')
plt.title('Bar Chart')
plt.show()