import pandas as pd
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

# 设置数据显示的编码格式为东亚宽度，以使列对齐
pd.set_option("display.unicode.east_asian_width", True)
# 读取Excel文件
df = pd.read_excel("datas/books.xlsx", sheet_name="Sheet2")
print(df)
# x轴和y轴数据
x = list(df["年份"])
y1 = list(df["京东"])
y2 = list(df["天猫"])
y3 = list(df["自营"])
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 创建柱状图并设置主题
# 为柱状图添加x轴和y轴数据
bar.add_xaxis(x)
bar.add_yaxis("京东", y1)
bar.add_yaxis("天猫", y2)
bar.add_yaxis("自营", y3)
# 渲染图表到HTML文件，存放在程序所在目录下
bar.render("Chapter 5/mybar1.html")
