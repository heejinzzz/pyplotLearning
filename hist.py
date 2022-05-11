import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#  导入中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

a = np.random.randint(70, 160, [250, ])

#  设置图片大小、分辨率
plt.figure(figsize=[12, 6], dpi=100)

#  传入数据和组数绘制直方图
# plt.hist(a, 8, color="green")
#  传入数据和每组的左端点绘制直方图
plt.hist(a, [10*i for i in range(7, 17)])

#  设置横坐标刻度
plt.xticks([10*i for i in range(7, 17)])

#  设置横纵坐标名、标题
plt.xlabel("电影时长（单位：分钟）", loc="center")
plt.ylabel("电影数", loc="top")
plt.title("250部电影时长", loc="center")

#  绘制网格及其透明度
plt.grid(alpha=0.5)

plt.show()
