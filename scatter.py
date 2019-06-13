# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2000)
y = np.random.standard_normal((1000, 2))
plt.figure(figsize=(7, 5))
plt.scatter(y[:, 0], y[:, 1], marker='o')
plt.grid(True)
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter Plot')
plt.show()
