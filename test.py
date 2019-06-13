import pandas as pd
import sys
from matplotlib.font_manager import FontProperties
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import csv

# 加载大文件
# csv.field_size_limit(sys.maxsize)

# with open ('result.txt','r') as file:
#     #用csv去读文件 有关csv文件的格式请自行科谱
#     #csv去读取文件并不只是读取以.csv结尾的文件，它只要满足是分隔数据格式就可以了，以逗号进行分隔的数据
#     plots = csv.reader(file, delimiter=',')
#     for row in plots:
#         print row


# ----
# np.loadtxt('example.txt', delimiter=',', unpack=True)
#
# plt.plot(x,y,label = 'Loaded from example.txt')

font = FontProperties(fname=r"SimHei.ttf", size=14)

df = DataFrame(np.random.randn(1024,7260))

plt.figure(figsize=(8, 6))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.subplots_adjust(left=.2, right=0.95, bottom=0.15, top=0.95)
plt.imshow(df)
plt.title('oneLat')
plt.colorbar(cax=None,ax=None,shrink=0.5)
plt.show()
plt.savefig("./oneLat.png")