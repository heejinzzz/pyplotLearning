import matplotlib.pyplot as plt

#  导入中文字体
plt.rcParams["font.sans-serif"] = "SimHei"

movie = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5：\n最后的骑士",
         "摔跤吧！爸爸", "加勒比海盗5：\n死无对证", "金刚：骷髅岛", "极限特工：\n终极回归", "生化危机6：\n终章"]
income = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12]

#  设置图片大小、分辨率
plt.figure(figsize=(15, 8), dpi=80)

#  传入横纵坐标的值来绘制横向的条形图，并设置柱形粗细
plt.barh(range(len(movie)), income, color="blue", height=0.4)

#  设置纵坐标刻度和标签
plt.yticks(range(len(movie)), movie)

#  设置横纵坐标名、标题
plt.ylabel("电影", loc="center")
plt.xlabel("票房（单位：亿）", loc="right")
plt.title("2017年内地电影票房前10名", loc="center")

plt.show()
