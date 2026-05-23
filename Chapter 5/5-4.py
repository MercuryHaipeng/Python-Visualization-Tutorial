import pandas as pd
from pyecharts.charts import Line
from pyecharts import options as opts

"""
================================
绘制折线图
================================ 
"""
df = pd.read_excel("datas/books.xlsx", sheet_name="Sheet2")
x = list(df["年份"].values.astype(str))     # 将年份列转换为字符串
y1 = list(df["京东"])
y2 = list(df["天猫"])
y3 = list(df["自营"])
line = Line()  # 创建折线图
# 为折线图添加x轴和y轴数据
line.add_xaxis(xaxis_data=x)
line.add_yaxis(series_name="京东", y_axis=y1)
line.add_yaxis(series_name="天猫", y_axis=y2)
line.add_yaxis(series_name="自营", y_axis=y3)
# 渲染图表到HTML文件，存放在程序所在目录下
line.render("Chapter 5/myline1.html")


"""
================================
绘制面积图 
================================ 
"""
df = pd.read_excel("datas/books.xlsx", sheet_name="Sheet2")
x = list(df["年份"].values.astype(str))
y1 = list(df["京东"])
y2 = list(df["天猫"])
y3 = list(df["自营"])
line = Line()  # 创建折线图
# 为折线图添加x轴、y轴数据并设置为面积图
line.add_xaxis(xaxis_data=x)
line.add_yaxis(series_name="京东", y_axis=y1, areastyle_opts=opts.AreaStyleOpts(opacity=1))
line.add_yaxis(series_name="天猫", y_axis=y2, areastyle_opts=opts.AreaStyleOpts(opacity=1))
line.add_yaxis(series_name="自营", y_axis=y3, areastyle_opts=opts.AreaStyleOpts(opacity=1))
# 渲染图表到HTML文件，存放在程序所在目录下
line.render("Chapter 5/myline2.html")