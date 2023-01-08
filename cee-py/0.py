# faawdd
# 2020.11.14
import pandas as pd
from pyecharts.charts import Map
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from pyecharts.globals import CurrentConfig, OnlineHostType

file = r'/home/faawdd/下载/工作簿1.xlsx'  # 目标文件
data2020 = pd.read_excel(file, sheet_name='Sheet1')  # 读取目标文件
provinces = data2020['省份'].value_counts().to_dict()  # 读取高校省份信息并转化为dict
provinces_items = list(provinces.items())  # 转换为list格式
for i in range(len(provinces_items)):  # 把这里面的每个tuple转换为list
    provinces_items[i] = list(provinces_items[i])


map1 = Map()  # 绘制各省高校数量地图，因为map在python中是保留字，所以变量名用map1
(
    map1.add("", data_pair=provinces_items, maptype="china")
    .set_global_opts(title_opts=opts.TitleOpts(title="国内各省普通高校数量\n（数据来源：http://www.moe.gov.cn/jyb_xxgk/s5743/s5744/202007/t20200709_470937.html）"),
                     tooltip_opts=opts.TooltipOpts(
                         trigger="item", formatter='{b}: {c}'),  # 设置鼠标提示信息
                     visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                       pieces=[{"max": 40, "min": 1, "label": "1-40"},
                                                               {"max": 80, "min": 41,
                                                                   "label": "41-80"},
                                                               {"max": 120, "min": 81,
                                                                   "label": "81-120"},
                                                               {"max": 160, "min": 121,
                                                                "label": "121-160"},
                                                               {"max": 200, "min": 161, "label": "161-200"}]
                                                       ))
    .render_notebook()
)

map1.render(path="cee-py/国内各省普通高校数量.html")
