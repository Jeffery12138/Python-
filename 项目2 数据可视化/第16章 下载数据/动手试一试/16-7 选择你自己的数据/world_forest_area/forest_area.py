import csv
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code


# 将csv数据加载到一个阅读器对象
filename = 'world_forest_area.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in range(5):
        header_row = next(reader)
    # print(header_row)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # 创建一个包含森林面积的字典
    forest_areas = {}
    for row in reader:
        country_name = row[0]
        forest_2016 = row[60]
        if forest_2016:
            forest_2016 = int(float(forest_2016))
            code = get_country_code(country_name)
            if code:
                forest_areas[code] = forest_2016

# print(forest_areas)
# 根据森林面积将所有的国家分成四组
forest_area_1, forest_area_2, forest_area_3, forest_area_4 = {}, {}, {}, {}
for cc, forest_area in forest_areas.items():
    if forest_area < 10000:
        forest_area_1[cc] = forest_area
    elif forest_area < 100000:
        forest_area_2[cc] = forest_area
    elif forest_area < 1000000:
        forest_area_3[cc] = forest_area
    else:
        forest_area_4[cc] = forest_area

# print(len(forest_area_1), len(forest_area_2), len(forest_area_3), len(forest_area_4))

wm_style = RS('#336699', base_style=LCS)

wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Forest Area (sq.km) in 2016, by Country'
wm.add('0-10k', forest_area_1)
wm.add('10k-0.1m', forest_area_2)
wm.add('0.1m-1m%', forest_area_3)
wm.add('>1m%', forest_area_4)

wm.render_to_file('world_forest_area.svg')