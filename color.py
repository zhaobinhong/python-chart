# -*- coding: utf-8 -*-
"""
"""
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# import numpy as np
#
# np.random.seed(20180316)
# x = np.random.randn(102, 72)
#
# f, (ax1, ax2) = plt.subplots(figsize=(6, 6), nrows=2)
#
# # sns.heatmap(x, annot=True, ax=ax1)
#
# sns.heatmap(x, annot=True, ax=ax2, annot_kws={'weight':'bold'})
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# 热力图
import matplotlib.cm as cm
from matplotlib.colors import LogNorm


# Function to get data
def get_data(file_name, hour):
    data = pd.read_csv(file_name)
    X_parameter = []
    Y_parameter = []
    Z_parameter = []
    coln = 'wind_' + str(hour)
    for x, y, z in zip(data['x'], data['y'], data[coln]):
        X_parameter.append(int(x))
        Y_parameter.append(int(y))
        Z_parameter.append(float(z))
    return X_parameter, Y_parameter, Z_parameter


# Function to show Thermodynamic diagram
def draw_thermodynamic_diagram(fileName, hour):
    print(fileName, hour)

    x, y, z = get_data(fileName, hour)
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)

    height = y_max - y_min + 1
    width = x_max - x_min + 1
    arr = np.zeros((height, width))  # arr 热力图中的值阵

    for i in range(len(x)):
        arr[y[i] - y_min, x[i] - x_min] = z[i]

    # 热力图默认左上为0,0
    # 所以热力图的显示和arr是一致的
    # 未解决以左下为0,0,
    plt.imshow(arr, extent=(np.amin(x), np.amax(x), np.amax(y), np.amin(y)),
               cmap=cm.hot, norm=LogNorm())
    plt.colorbar()
    plt.savefig(fileName + '_h' + str(hour) + '.png')  # 先存，再show
    plt.show()

    return


for date in range(1, 6):
    fileName = 'compress_reProcess_day' + str(date) + '.csv'
    for hour in range(9, 21):
        draw_thermodynamic_diagram(fileName, hour)