import csv
import pygal_maps_world.maps
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

from country_codes import get_country_code


# 将csv数据加载到一个阅读器对象
filename = 'world_rural_population.csv'
with open(filename, encoding='utf-8') as f:
    reader = csv.reader(f)
    for i in range(5):
        header_row = next(reader)

    # 创建一个包含乡村人口的字典
    rural_populations = {}
    for row in reader:
        country_name = row[0]
        population_2019 = row[63]
        if population_2019:
            population_2019 = int(float(population_2019))
            code = get_country_code(country_name)
            if code:
                rural_populations[code] = population_2019

# 根据乡村人口数量将所有的国家分成三组
rural_pops_1, rural_pops_2, rural_pops_3, rural_pops_4 = {}, {}, {}, {}
for rural, pop in rural_populations.items():
    if pop < 10:
        rural_pops_1[rural] = pop
    elif pop < 30:
        rural_pops_2[rural] = pop
    elif pop < 50:
        rural_pops_3[rural] = pop
    else:
        rural_pops_4[rural] = pop

wm_style = RS('#336699', base_style=LCS)

wm = pygal_maps_world.maps.World(style=wm_style)
wm.title = 'World Rural Population (% of total population) in 2019, by Country'
wm.add('0-10%', rural_pops_1)
wm.add('10%-30%', rural_pops_2)
wm.add('30%-50%', rural_pops_3)
wm.add('>50%', rural_pops_4)

wm.render_to_file('world_rural_population.svg')