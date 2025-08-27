import matplotlib.pyplot as plt
import seaborn as sns
categories = ['A' ,'B','C','D','E','F','G','H']
values = [2,3,4,5,6,7,8,9,15]
plt.xlabel('categories')
plt.ylabel('values')
sns.histplot(categories, bins=5, color='skyblue')
plt.figure(figsize=(4,4))
plt.title('Bar Chart')
plt.show()