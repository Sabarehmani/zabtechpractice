import matplotlib.pyplot as plt
import numpy as np
X_values=(2,3,4,5,6,7)
Y_values=(2,3,4,5,6,7)
plt.xlabel('X_axis Label')
plt.ylabel('y_axis Label')
plt.title('Line Chart')
plt.plot(X_values,Y_values,marker='o',linestyle='-',color='blue')
plt.show()


