import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 搜索有关仓库的信息
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

print(plot_dicts)
# 可视化

my_config = pygal.Config()

my_config.style = LS('#336699', base_style=LCS)

my_config.style.title_font_size = 24
my_config.style.label_font_size = 14    # 副标签时x轴上的项目名以及y轴上的大部分数字
my_config.style.major_label_font_size = 18  # 主标签是y轴上为5000整数倍的刻度


my_config.x_label_rotation = 45
my_config.show_legend = False

# 将标签截断为15个字符,如果将鼠标指向被截断的标签，将显示完整标签
my_config.truncate_label = 15
# 隐藏图表中的水平线（y guide lines）
my_config.show_y_guides = False
# 图标宽度，默认800
my_config.width = 1000

chart = pygal.Bar(my_config)

chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)

chart.render_to_file('python_repos.svg')