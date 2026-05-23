import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

from pyecharts.charts import Boxplot

from pyecharts.charts import EffectScatter

"""
================================
绘制饼图
================================ 
"""
df = pd.read_excel("datas/data3.xlsx")
x_data = df["地区"]
y_data = df["销量"]
# 将数据转换为列表加元组的格式（[(key1, value1), (key2, value2)]）
data = [list(z) for z in zip(x_data, y_data)]
# 数据排序
data.sort(key=lambda x: x[1])
print(x_data)
print(data)
pie = Pie()  # 创建饼形图
# 为饼形图添加数据
pie.add(
    series_name="地区",  # 序列名称
    data_pair=data,  # 数据
)
pie.set_global_opts(
    # 饼形图标题居中
    title_opts=opts.TitleOpts(title="各地区销量情况分析", pos_left="center"),
    # 不显示图例
    legend_opts=opts.LegendOpts(is_show=False),
)
pie.set_series_opts(
    # 序列标签
    label_opts=opts.LabelOpts(),
)
# 渲染图表到HTML文件，存放在程序所在目录下
pie.render("Chapter 5/mypie1.html")


"""
================================
绘制箱线图
================================ 
"""
# 读取Excel文件
df = pd.read_excel("datas/tips.xlsx")
y_data = [list(df["总消费"])]
boxplot = Boxplot()  # 创建箱形图
# 为箱形图添加数据
boxplot.add_xaxis([""])
boxplot.add_yaxis("", y_axis=boxplot.prepare_data(y_data))
# 渲染图表到HTML文件，存放在程序所在目录下
boxplot.render("Chapter 5/myboxplot.html")


"""
================================
绘制涟漪特效散点图
================================ 
"""
# 读取Excel文件
df = pd.read_excel("datas/books.xlsx", sheet_name="Sheet2")
# x轴和y轴数据
x = list(df["年份"].values.astype(str))
y1 = list(df["京东"])
y2 = list(df["天猫"])
y3 = list(df["自营"])
# 绘制涟漪散点图
scatter = EffectScatter()
scatter.add_xaxis(x)
scatter.add_yaxis("", y1)
scatter.add_yaxis("", y2)
scatter.add_yaxis("", y3)
# 渲染图表到HTML文件，存放在程序所在目录下
scatter.render("Chapter 5/myscatter.html")