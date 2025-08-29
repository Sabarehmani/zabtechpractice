import matplotlib.pyplot as plt

# Sample data
data = [12, 15, 20, 21, 21, 23, 24, 25, 25, 25, 26, 27, 30, 31, 32, 33, 35, 36, 40]

# Create histogram
plt.hist(data, bins=8, edgecolor='black', alpha=0.7)

# Add labels and title
plt.xlabel("students")
plt.ylabel("pass/fail")
plt.title("Histogram Example")

# Show chart
plt.show()
