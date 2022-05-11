import matplotlib.pyplot as plt


#  导入中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22, 23]
b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 25, 11, 15, 5, 13, 17, 10, 11, 13, 12, 13, 6]

x1 = list(range(31))
x2 = list(range(40, 71))

#  设置图片大小、分辨率
plt.figure(figsize=(12, 5), dpi=100)

#  传入横纵坐标的值来绘制散点图
plt.scatter(x1, a, color="blue", label="3月")
plt.scatter(x2, b, color="orange", label="10月")

#  设置横坐标刻度与标签
x_label = ["3月{}日".format(i+1) for i in x1] + ["10月{}日".format(i % 39) for i in x2]
x_label = x_label[::2]
plt.xticks((x1+x2)[::2], x_label, rotation=45)

#  设置纵坐标刻度与标签
y_label = ["{}度".format(i) for i in range(30)]
plt.yticks(range(30), y_label)

#  设置横纵坐标名和图片标题
plt.xlabel("日期", loc="right")
plt.ylabel("最高气温", loc="top")
plt.title("北京2016年3、10月每天白天最高气温", loc="center")

#  添加图例，显示label
plt.legend()

#  显示图片
plt.show()
