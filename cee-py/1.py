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
locations_dict = data2020['所在地'].value_counts().to_dict()  # 读取所在地的信息
locations_items = list(locations_dict.items())  # 转换成list格式
locations_items.remove(('克孜勒苏柯尔克孜自治州', 1))  # 去掉该数据
locations_items.remove(('铁门关市', 1))  # 去掉该数据
geo = Geo()
(
    geo.add("", data_pair=locations_items, type_="scatter", symbol_size=5)
    .add_schema(maptype='china')
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="国内各主要城市高校分布 \n（数据来源：http://www.moe.gov.cn/jyb_xxgk/s5743/s5744/202007/t20200709_470937.html）"),
                     visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                                                       pieces=[{"max": 20, "min": 1, "label": "1-20"},
                                                               {"max": 40, "min": 21,
                                                                   "label": "21-40"},
                                                               {"max": 60, "min": 41,
                                                                   "label": "41-60"},
                                                               {"max": 80, "min": 61,
                                                                "label": "61-80"},
                                                               {"max": 100, "min": 81, "label": "81-100"}]
                                                       ))
    .render_notebook()
)
geo.render(path="cee-py/国内各主要城市高校分布.html")
