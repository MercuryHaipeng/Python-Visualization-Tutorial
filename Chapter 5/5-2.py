from pyecharts.charts import Bar  # 从Pyecharts模块导入Bar对象
from pyecharts import options as opts

bar = Bar()
# 为柱状图添加数据
bar.add_dataset(
    source=[
        ["val", "销量", "月份"],
        [24, 10009, "1月"],
        [57, 19988, "2月"],
        [74, 39870, "3月"],
        [50, 12345, "4月"],
        [99, 50145, "5月"],
        [68, 29146, "6月"],
    ]
)
bar.add_yaxis(
    series_name="销量",                         # 系列名称
    y_axis=[],                                  # 系列数据
    encode={"x": "销量", "y": "月份"},          # 对x轴y轴数据进行编码
    label_opts=opts.LabelOpts(is_show=False),   # 不显示标签文本
)
bar.set_global_opts(
    title_opts=opts.TitleOpts(
        title="线上图书月销量分析",              # 主标题
        subtitle="月销量",                      # 副标题
        pos_left="15%",                     # 主标题居中
    ),  
    xaxis_opts=opts.AxisOpts(name="销量"),      # x轴坐标轴名称
    yaxis_opts=opts.AxisOpts(type_="category"), # y轴坐标轴类型为"类目"
# 图例设置在右上方
    legend_opts=opts.LegendOpts(
        pos_top="5%",      # 距顶部 10%
        pos_left="center", # 居中
    ),
    # 视觉映射
    visualmap_opts=opts.VisualMapOpts(
        orient="vertical",                      # 垂直放置颜色条
        pos_right=20,                           # 距右边 20px
        pos_top=100,                            # 距顶部 100px
        min_=10,                                # 颜色条最小值
        max_=100,                               # 颜色条最大值
        range_text=["High", "Low"],             # 颜色条两端的文本
        dimension=0,                            # 颜色条映射的维度
        range_color=["#FFF0F5", "#8B008B"],     # 颜色范围
    ),
    # 设置工具箱
    toolbox_opts=opts.ToolboxOpts(is_show=True,     # 显示工具箱
                                  pos_left="600"),  # 距离左边600px
    # 区域缩放工具条
    datazoom_opts=opts.DataZoomOpts()
)
bar.render("Chapter 5/mycharts2.html")  # 生成图表
