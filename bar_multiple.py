import matplotlib.pyplot as plt

#  导入中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

movie = ["猩球崛起3：\n终极之战", "敦刻尔克", "蜘蛛侠：\n英雄归来", "战狼2"]
income1 = [15746, 312, 4497, 319]
income2 = [12357, 156, 2045, 168]
income3 = [2358, 399, 2358, 362]
x1 = [5*i for i in range(4)]
x2 = [5*i+1 for i in range(4)]
x3 = [5*i+2 for i in range(4)]

#  设置图片大小、分辨率
plt.figure(figsize=(15, 8), dpi=80)

#  传入横纵坐标的值来绘制多柱形条形图，并设置柱形粗细
plt.bar(x1, income1, color="blue", label="2017年9月14日")
plt.bar(x2, income2, color="green", label="2017年9月15日")
plt.bar(x3, income3, color="yellow", label="2017年9月16日")

#  设置横坐标刻度和标签
plt.xticks(x2, movie)

#  设置横纵坐标名、标题
plt.xlabel("电影", loc="center")
plt.ylabel("票房（单位：万）", loc="top")
plt.title("当日热映电影连续三天票房", loc="center")

#  绘制网格及其透明度
plt.grid(alpha=0.4)

#  添加图例，显示label
plt.legend()

plt.show()
