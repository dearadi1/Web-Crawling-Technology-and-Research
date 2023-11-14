import pandas as pd
from pyecharts import *

df = pd.read_csv(r"数据爬虫程序\lianjia\output\ershoufang.csv")
# 分析前处理
df.drop("id", axis=1, inplace=True)
df.drop("单价", axis=1, inplace=True)
df.drop("户型结构", axis=1, inplace=True)
df.drop("套内面积", axis=1, inplace=True)
df.drop("建筑类型", axis=1, inplace=True)
df.drop("建筑结构", axis=1, inplace=True)
df.drop("梯户比例", axis=1, inplace=True)
df.drop("产权年限", axis=1, inplace=True)
df.drop("挂牌时间", axis=1, inplace=True)
df.drop("交易权属", axis=1, inplace=True)
df.drop("上次交易", axis=1, inplace=True)
df.drop("房屋用途", axis=1, inplace=True)
df.drop("房屋年限", axis=1, inplace=True)
df.drop("产权所属", axis=1, inplace=True)
df.drop("抵押信息", axis=1, inplace=True)
df.drop("房本备件", axis=1, inplace=True)
df.drop("26", axis=1, inplace=True)
df.drop("27", axis=1, inplace=True)
df.drop("28", axis=1, inplace=True)
df.drop("29", axis=1, inplace=True)
df.columns = ["小区", "市区", "价格", "户型", "楼层", "面积", "朝向", "装修", "电梯"]
df=df.loc[df["面积"]!="南 北"]
df["面积"] = df["面积"].str.replace("㎡", "").astype(float)
df["楼层"] = df["楼层"].str.replace(r"\(.*\)", "", regex=True)
df["电梯"] = df["电梯"].str.replace("暂无数据", "未知")

# 缺失值处理
df["小区"].fillna("未知", inplace=True)
df["市区"].fillna("未知", inplace=True)
df["价格"].fillna("未知", inplace=True)
df["户型"].fillna("未知", inplace=True)
df["楼层"].fillna("未知", inplace=True)
df["面积"].fillna("未知", inplace=True)
df["朝向"].fillna("未知", inplace=True)
df["装修"].fillna("未知", inplace=True)
df["电梯"].fillna("未知", inplace=True)

# 房屋朝向数据修改
df["朝向"] = df["朝向"].str.replace("南 北", "南")
df["朝向"] = df["朝向"].str.replace("东 北", "东北")
df["朝向"] = df["朝向"].str.replace("东 西", "东")
df["朝向"] = df["朝向"].str.replace("南 西 北", "西")
df["朝向"] = df["朝向"].str.replace("西 东", "东")
df["朝向"] = df["朝向"].str.replace("东南 西北", "未知")
df["朝向"] = df["朝向"].str.replace("西 北", "西北")
df["朝向"] = df["朝向"].str.replace("南 西", "西南")
df["朝向"] = df["朝向"].str.replace("南 北 西", "西")
df["朝向"] = df["朝向"].str.replace("北 西", "西北")
df["朝向"] = df["朝向"].str.replace("东 南", "东南")

df.to_csv(r"数据分析程序\output\ershoufang_按需处理后.csv")
print(df.head())
# 按区分组
g = df.groupby("市区")
# 统计二手房城区数据
df_region = g.count()["小区"]

# map可视化
x = df_region.index.tolist()
y = df_region.values.tolist()
new_x = [x + "区" for x in x]
from pyecharts import options as opts
from pyecharts.charts import Map

m = (
    Map()
    .add("哈尔滨", [list(z) for z in zip(new_x, y)], "哈尔滨")
    .set_global_opts(
        title_opts=opts.TitleOpts(title="哈尔滨二手房各区分布"),
        visualmap_opts=opts.VisualMapOpts(max_=3000),
    )
)
# m.render_notebook()
m.render(r"数据分析程序\output\ershoufang_房屋数量_map.html")

# 价格最低的15套
from pyecharts.charts import Bar

top_price = df.sort_values("价格")[:15]
acea = top_price["小区"].values.tolist()
count = top_price["价格"].values.tolist()
bar = Bar().add_xaxis(acea).add_yaxis("价格(万\元)", count)
bar.render(r"数据分析程序\output\ershoufa_最便宜_bar.html")

from pyecharts.charts import Scatter

# 总价二手散点图
s = (
    Scatter()
    .add_xaxis(df["面积"].values.tolist())
    .add_yaxis("", df["价格"].values.tolist())
    .set_global_opts(xaxis_opts=opts.AxisOpts(type_="value"))
)
s.render(r"数据分析程序\output\总价二手散点图.html")


# 装修情况/有无电梯玫瑰图
g1 = df.groupby("装修")
g2 = df.groupby("电梯")
df_fitment = g1.count()["小区"]
df_direction = g2.count()["小区"]

fitment = df_fitment.index.tolist()
count1 = df_fitment.values.tolist()

directions = df_direction.values.tolist()
count2 = df_direction.values.tolist()

bar = (
    Bar()
    .add_xaxis(fitment)
    .add_yaxis("", count1, category_gap="50%")
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(name="数量"),
        title_opts=opts.TitleOpts(title="装修情况/有无电梯玫瑰图", pos_left="33%", pos_top="5%"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_left="90%", pos_top="58%", orient="vertical"
        ),
    )
)
from pyecharts.charts import Pie

c2 = (
    Pie(init_opts=opts.InitOpts(width="800px", height="600px"))
    .add(
        "",
        [list(z) for z in zip(directions, count2)],
        radius=["10%", "30%"],
        center=["75%", "65%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="有/无电梯", pos_left="33%", pos_top="5%"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_left="90%", pos_top="15%", orient="vertical"
        ),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{c}\n({d}%)"), position="outside"
    )
)
bar.overlap(c2)
bar.render(r"数据分析程序\output\装修情况_有无电梯玫瑰图.html")


# 二手房楼层分布柱状缩放图
g = df.groupby("楼层")
df_floor = g.count()["小区"]

floor = df_floor.index.tolist()
count = df_floor.values.tolist()
bar = (
    Bar()
    .add_xaxis(floor)
    .add_yaxis("数量", count)
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="二手房楼层分布柱状缩放图"),
        yaxis_opts=opts.AxisOpts(name="数量"),
        xaxis_opts=opts.AxisOpts(name="楼层"),
        datazoom_opts=opts.DataZoomOpts(type_="slider"),
    )
)
bar.render(r"数据分析程序\output\二手房楼层分布柱状图.html")


# 房屋面积的柱状分析图

area_level = [0, 50, 100, 150, 200, 250, 300, 350, 400, 1500]
label_level = [
    "小于50",
    "50-100",
    "100-150",
    "150-200",
    "200-250",
    "250-300",
    "300-350",
    "350-400",
    "大于400",
]
jzmj_cut = pd.cut(df["面积"], area_level, labels=label_level)
df_area = jzmj_cut.value_counts()
area = df_area.index.tolist()
count = df_area.values.tolist()

bar = (
    Bar()
    .add_xaxis(area)
    .add_yaxis("数量", count)
    .reversal_axis()
    .set_series_opts(label_opts=opts.LabelOpts(position="right"))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="房屋面积分布纵向柱状图"),
        yaxis_opts=opts.AxisOpts(name="面积"),
        xaxis_opts=opts.AxisOpts(name="数量"),
    )
)
bar.render(r"数据分析程序\output\房屋面积的柱状分析图.html")


# 房屋朝向饼图
g = df.groupby("朝向")
df_direction = g.count()["小区"]

directions = df_direction.index.tolist()
count = df_direction.values.tolist()

c1 = (
    Pie(init_opts=opts.InitOpts(width="800px", height="600px"))
    .add(
        "",
        [list(z) for z in zip(directions, count)],
        radius=["20%", "60%"],
        center=["40%", "50%"],
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="房屋朝向占比", pos_left="33%", pos_top="5%"),
        legend_opts=opts.LegendOpts(
            type_="scroll", pos_left="80%", pos_top="25%", orient="vertical"
        )
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}:{c} ({d}%)", position="outside")
    )
)

# 保存为HTML文件
c1.render(r"数据分析程序\output\房屋朝向占比.html")