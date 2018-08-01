# zc-cris

import csv
from datetime import datetime

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

file_name = "../file/cd_weather_2014.csv"
with open(file_name) as file:
    reader = csv.reader(file)
    # 读取标题行
    content = next(reader)
    # 特征（列）的索引从0开始
    # for index, column in enumerate(content):
    #     print(index, column)

    # 提取每行第一列的时间和第二列的温度
    high_temperature, dates, low_temperature = [], [], []
    for row in reader:
        date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(date)

        content = int(row[1])
        high_temperature.append(content)

        content = int(row[3])
        low_temperature.append(content)

# 设置图片的分辨率和大小？
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, high_temperature, c='red', linewidth='1', alpha=0.5)
plt.plot(dates, low_temperature, c='blue', linewidth='1', alpha=0.5)
plt.fill_between(dates, high_temperature, low_temperature, facecolor='blue', alpha=0.1)

plt.title("成都2014年气温变化表", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('气温(F)', fontsize=16)
# 使x轴的刻度倾斜
fig.autofmt_xdate()
plt.tick_params(axis='both', labelsize=16)
plt.show()
