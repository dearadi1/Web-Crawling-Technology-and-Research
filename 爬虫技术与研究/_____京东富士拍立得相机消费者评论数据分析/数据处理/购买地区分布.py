import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ThemeType

# 读取数据
data = pd.read_csv(r"datas\new_file\计算后.csv")

# 添加省份信息到location列
data["location"] = data["location"] + "省"

# 统计各个地区的数量
location_count = data["location"].value_counts().reset_index()
location_count.columns = ["location", "count"]

# 绘制地图
c = (
    Map(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add(
        "购买地分布",
        [list(z) for z in zip(location_count["location"], location_count["count"])],
        "china",
        is_map_symbol_show=False,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国各地区分布"),
        visualmap_opts=opts.VisualMapOpts(
            max_=location_count["count"].max(), is_piecewise=True
        ),
    )
)
c.render(r"datas\html\location_distribution.html")
