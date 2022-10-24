import json

import requests  # 倒入requests库
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)


url = "https://oxygennotincluded.fandom.com/zh/wiki/%E9%A6%96%E9%A1%B5"  # 请求地址缺氧wiki首页
response = requests.get(url=url)  # 返回结果
wb_data = response.text  # 文本展示返回结果
html = etree.HTML(wb_data)  # 将页面转换成文档树
Category_Name = html.xpath('//*[@id="gallery-0"]/div/div[2]/a')  # 获取分类的文本名称
# Category_href = html.xpath('//*[@id="gallery-0"]/div/div[2]/a/@href')  # 获取分类的href链接
response.close()


def get_nan(self):
    # 构造一个空列表，来管理所以数据
    dic_list = []
    # 拼接的html头
    base_url = 'https://oxygennotincluded.fandom.com'
    # 每一次循环，表示对一个分类的信息进行提取
    for hypoxia in Category_Name:
        title = hypoxia.xpath('./text()')[0]  # 获取名称并且提取列表内的内容
        href = hypoxia.xpath('./@href')[0]  # 获取href并且提取列表内的内容
        detail_url = base_url + href  # 做拼接把前域名和href拼接起来
        # 字典
        dic = {'name': title,
               'href': detail_url
               }
        dic_list.append(dic)  # 装到列表里面

    json_str = json.dumps(dic_list)  # 使用用json.dump()编码
    aa = json.loads(json_str)[self]  # 使用json.load() 解码
    aac = aa['href']
    return aac