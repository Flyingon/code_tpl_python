import requests
import numpy as np
import io
import pandas as pd
import matplotlib.pyplot as plt

txt_url = 'https://www.tzspace.cn/csv/ex1data1.txt'
content = requests.get(txt_url).text
buf = io.StringIO(content)

l = buf.readline()
# l = f.readline()

xy = np.zeros((2, 97))
print("xy shape:", xy.shape)

a = 0
while l:
    l2 = l.split(",")
    f1 = float(l2[0])
    f2 = float(l2[1])
    xy[0, a] = f1
    xy[1, a] = f2
    a += 1
    l = buf.readline()

# f.close()

# print(xy)

plt.clf()

plt.figure('Scatter', facecolor='lightgray')
plt.title('Scatter', fontsize=20)
plt.xlabel('Population of City in 10,000s', fontsize=7)  # 水平坐标
plt.ylabel('Profit in $10,000', fontsize=7)  # 垂直坐标
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.scatter(xy[0, :], xy[1, :], s=60, cmap='jet_r', alpha=0.5, marker='o')
# scatter画散点图  c=d 颜色=距离要与cmap(颜色映射)同用,正向映射(jet)反向(jet_r),alpha透明度,marker图形（*，d..）
plt.show()

_dci_ = plt.show()


def gradient_descent(train_data):
    m = train_data.shape[1]  #
    alpha = 0.01  # learning rate
    theta0 = 10.
    theta1 = 8.
    J_theta = 0.
    #     print(m)
    for i in range(20):
        theta0_tmp = theta0
        theta0 = theta0 - alpha * 1 / m * np.sum((theta0 + theta1 * train_data[0, :] - train_data[1, :]) * 1)
        theta1 = theta1 - alpha * 1 / m * np.sum(
            (theta0_tmp + theta1 * train_data[0, :] - train_data[1, :]) * train_data[0, :])
        J_theta = 1 / (2 * m) * np.sum(np.square(theta0 + theta1 * train_data[0, :] - train_data[1, :]))
        print(i, J_theta)

    #    print(theta0, theta1)
    return theta0, theta1


theta = gradient_descent(xy)

plt.clf()

plt.figure('Scatter', facecolor='lightgray')
plt.title('Scatter', fontsize=20)
plt.xlabel('Population of City in 10,000s', fontsize=7)  # 水平坐标
plt.ylabel('Profit in $10,000', fontsize=7)  # 垂直坐标
plt.tick_params(labelsize=10)
plt.grid(linestyle=':')
plt.scatter(xy[0, :], xy[1, :], s=60, cmap='jet_r', alpha=0.5, marker='x')
# scatter画散点图  c=d 颜色=距离要与cmap(颜色映射)同用,正向映射(jet)反向(jet_r),alpha透明度,marker图形（*，d..）
x = np.linspace(np.min(xy[0, :]), np.max(xy[0, :]), 100)
y = theta[0] + theta[1] * x
plt.plot(x, y, c='black')
plt.show()

_dci_ = plt.show()
