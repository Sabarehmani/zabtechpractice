# import matplotlib.pyplot as plt
import numpy as np

# # # Example: dataset distribution
# # data = np.random.randn(1000)  # fake dataset
# # plt.hist(data, bins=30, color='blue', alpha=0.7)
# # plt.title("Data Distribution")
# # plt.show()
# epochs = [1,2,3,4,5]
# loss = [0.9, 0.6, 0.4, 0.3, 0.2]
# accuracy = [0.5, 0.65, 0.75, 0.85, 0.9]

# plt.plot(epochs, loss, label="Loss", marker='o')
# plt.plot(epochs, accuracy, label="Accuracy", marker='s')
# plt.xlabel("Epochs")
# plt.ylabel("Value")
# plt.title("Training Progress")
# plt.legend()
# plt.show()

# import seaborn as sns
# import numpy as np

# # Example confusion matrix
# cm = np.array([[50, 2], [3, 45]])  

# sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
# plt.title("Confusion Matrix")
# plt.xlabel("Predicted")
# plt.ylabel("Actual")
# plt.show()

# import matplotlib.pyplot as plt

# img = np.random.rand(28,28)  # fake image (28x28 like MNIST)

# plt.imshow(img, cmap="gray")
# plt.title("Predicted: 7")
# plt.show()
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]
plt.plot(x, y, marker='o')
plt.title("Simple Visualization")
plt.show()
