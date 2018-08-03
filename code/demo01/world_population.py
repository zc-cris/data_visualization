# zc-cris
import json

import pygal_maps_world.maps
from pygal_maps_world.i18n import COUNTRIES


# 获取两个字母的不国家编码和国家名字
# for code in sorted(COUNTRIES.keys()):
#     print(code, COUNTRIES[code])

def get_code(country_name):
    # 遍历字典的键值对，需要加上items()
    for code, name in COUNTRIES.items():
        if country_name == name:
            return code
    return None


dic1 = {}
dic2 = {}
dic3 = {}
with open("../file/population_data.json") as file:
    json_load = json.load(file)
    for i in json_load:
        if i['Year'] == '2010':
            # 对于字符串类型的小数，先float然后在int
            population = int(float(i['Value']))
            code = get_code(i['Country Name'])
            if code:
                if population < 10000000:
                    dic1[code] = population
                elif population < 1000000000:
                    dic2[code] = population
                else:
                    dic3[code] = population
            else:
                print("没有对应的国家码", i['Country Name'])

# 使用模块画出世界地图
worldmap = pygal_maps_world.maps.World()
worldmap.title = '2010 world population'
worldmap.add('小于1000万', dic1)
worldmap.add('1000万到10亿', dic2)
worldmap.add('大于10亿', dic3)
worldmap.render_to_file('americas.svg')
