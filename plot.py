import matplotlib.pyplot as plt


#  导入中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

x = list(range(11, 31))
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
z = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#  设置图片大小、分辨率
plt.figure(figsize=(10, 6), dpi=80)

#  传入横纵坐标的值来绘制折线图
plt.plot(x, y, color="red", label="小明")
plt.plot(x, z, color="green", label="小王")

#  设置横坐标刻度和标签
_x = x[::2]
label_x = ["{}岁".format(i) for i in _x]
plt.xticks(_x, label_x)

#  设置纵坐标刻度和标签
_y = list(range(8))
label_y = ["{}个".format(i) for i in _y]
plt.yticks(_y, label_y)

#  设置横纵坐标名、标题
plt.xlabel("年龄", loc="right")
plt.ylabel("交友数", loc="top")
plt.title("不同年龄段的交友数量", loc="center")

#  绘制网格及其透明度
plt.grid(alpha=0.5)

#  添加图例，显示label
plt.legend()

#  显示图片
plt.show()
