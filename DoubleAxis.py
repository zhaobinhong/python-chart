# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2000)
y = np.random.standard_normal((10, 2))

fig, ax1 = plt.subplots()  # 关键代码1 plt first data set using first (left) axis

plt.plot(y[:, 0], lw=1.5, label='1st')

plt.plot(y[:, 0], 'ro')
plt.grid(True)
plt.legend(loc=0)  # 图例位置自动
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value')
plt.title('A simple plot')

ax2 = ax1.twinx()  # 关键代码2  plt second data set using second(right) axis
plt.plot(y[:, 1], 'g', lw=1.5, label='2nd')
plt.plot(y[:, 1], 'ro')
plt.legend(loc=0)
plt.ylabel('value 2nd')
plt.show()
