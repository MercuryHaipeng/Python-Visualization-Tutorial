import pyecharts
from pyecharts.charts import Bar  # 从Pyecharts模块导入Bar对象
from pyecharts import options as opts  # 从pyecharts库中导入options模块
from pyecharts.globals import ThemeType

print(pyecharts.__version__)    # 2.1.0

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))  # 浅色主题
    # x轴和y轴数据
    .add_xaxis(["1月", "2月", "3月", "4月", "5月", "6月"])
    .add_yaxis("零基础学Python", [2567, 1888, 1359, 3400, 4050, 5500])
    .add_yaxis("Python数据分析技术手册", [1567, 988, 2270, 3900, 2750, 3600])
    # 设置图表标题
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热门图书销量分析",  # 主标题
            padding=[10, 4, 5, 90],  # 标题内边距
            subtitle="热门图书",  # 副标题
            item_gap=5,  # 主标题与副标题间距
            title_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18),
        ),  # 主标题样式
        # 设置图例
        legend_opts=opts.LegendOpts(
            pos_right=50,  # 图例与容器右侧的距离
            item_width=45,  # 图例项的宽度
            legend_icon="circle",
        ),  # 图例项的形状为圆形
        # 提示框
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",  # 坐标轴触发
            trigger_on="click",  # 鼠标点击触发
            axis_pointer_type="cross",  # 十字线指示器
            background_color="orange",  # 背景颜色为橙色
            border_width=2,  # 边框宽度为2
            border_color="red",
        ),  # 边框颜色为红色
    )
    .render("Chapter 5/mycharts1.html")
)
