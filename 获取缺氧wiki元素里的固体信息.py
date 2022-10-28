from cgitb import html
# from distutils.filelist import findall
from gettext import find
import json
from msilib.schema import Font
import re
from tkinter import font
from unittest import result
from webbrowser import get

import requests
import requests  # 倒入requests库
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)
from bs4 import BeautifulSoup





url = 'https://oxygennotincluded.fandom.com/zh/wiki/%E5%85%83%E7%B4%A0'  # 请求地址缺氧wiki里的元素类

Subpage = requests.get(url)  # 拼接后的url
html = etree.HTML(Subpage.text)

aww = input("请输入")
def href_page_text():
    href_ = html.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td/table/tbody/tr/td/div/span/a[@title="名"]'.replace("名",f"{aww}"))
    for href_a in href_:
        href_b = href_a.xpath('./@href')[0]
        get_url_tow = 'https://oxygennotincluded.fandom.com'  # url拼接
        href_Subpage = get_url_tow + href_b  # 调取href下的链接并拼接url
        href_Subpage = requests.get(href_Subpage)
        href_Subpage_text = href_Subpage.text
        # print(href_Subpage)

        return href_Subpage_text



href_page_text = href_page_text()




def massage_txt():
    # 把源码交给bs
    main_page_see = BeautifulSoup(href_page_text, "html.parser")
    # 找到描述文本
    meat_txt = main_page_see.find("meta", {"property": "og:description"}).get("content")
    return meat_txt
# print(massage_txt())







# 拿到标题名称
def massage_to():
    main_page_see = BeautifulSoup(href_page_text, 'lxml')
    meat_specific_heat = (main_page_see.select("aside h2")[0].string)# 标题
    return meat_specific_heat
Labe = massage_to()



# 拿到固体分类名称
def massage_tag():
    main_page_see = BeautifulSoup(href_page_text, 'lxml')
    meat_specific_heat = (main_page_see.select("aside div h3")[0].string)# 比热
    meat_thermal_conductivity = (main_page_see.select("aside div h3")[1].string)# 导热率
    meat_molar_mass = (main_page_see.select("aside div h3")[2].string)# 摩尔质量
    meat_light_absorption = (main_page_see.select("aside div h3")[3].text)#  光吸收率
    meat_radiation = (main_page_see.select("aside div h3")[4].string)# 辐射吸收因数
    meat_hardness = (main_page_see.select("aside div h3")[5].string)# 硬度
    meat_Classification= (main_page_see.select("aside div h3")[6].string)# 分类
    meat_Label = (main_page_see.select("aside div h3")[7].string)# 标签
    meat_transition = (main_page_see.select("aside div h3")[8].string)# 高温相变温度
    meat_meat_transition2 = (main_page_see.select("aside div h3")[9].string)# 高温相变产物
    meat_max_quality = (main_page_see.select("aside div h3")[10].string)# 单格最大质量
    return (meat_specific_heat,meat_thermal_conductivity,meat_molar_mass,meat_light_absorption,
            meat_radiation,meat_hardness,meat_Classification,meat_Label,meat_transition,
            meat_meat_transition2,meat_max_quality)
a = massage_tag()[0]
b = massage_tag()[1]
c = massage_tag()[2]
d = massage_tag()[3]
e = massage_tag()[4]
f = massage_tag()[5]
g = massage_tag()[6]
h = massage_tag()[7]
i = massage_tag()[8]
j = massage_tag()[9]
k = massage_tag()[10]

# print(d)


# 拿到各个固体分类里面的数据
def massage_tag_data():
    main_page_see = BeautifulSoup(href_page_text, 'lxml')
    meat_specific_heat = (main_page_see.select("aside div div ")[0].text)# 比热
    meat_thermal_conductivity = (main_page_see.select("aside div div")[1].text)# 导热率
    meat_molar_mass = (main_page_see.select("aside div div")[2].text)# 摩尔质量
    meat_light_absorption = (main_page_see.select("aside div div")[3].text)#  光吸收率
    meat_radiation = (main_page_see.select("aside div div")[4].text)# 辐射吸收因数
    meat_hardness = (main_page_see.select("aside div div")[5].text)# 硬度
    meat_Classification= (main_page_see.select("aside div div")[6].text)# 分类
    meat_Label = (main_page_see.select("aside div div")[7].text)# 标签
    meat_transition = (main_page_see.select("aside div div")[8].text)# 高温相变温度
    meat_meat_transition2 = (main_page_see.select("aside div div")[9].text)# 高温相变产物
    meat_max_quality = (main_page_see.select("aside div div")[10].text)# 单格最大质量
    return (meat_specific_heat,meat_thermal_conductivity,meat_molar_mass,meat_light_absorption,
            meat_radiation,meat_hardness,meat_Classification,meat_Label,meat_transition,
            meat_meat_transition2,meat_max_quality)


l = massage_tag_data()[0]
m = massage_tag_data()[1]
n = massage_tag_data()[2]
o = massage_tag_data()[3]
p = massage_tag_data()[4]
q = massage_tag_data()[5]
r = massage_tag_data()[6]
s = massage_tag_data()[7]
t = massage_tag_data()[8]
u = massage_tag_data()[9]
v = massage_tag_data()[10]



import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    data = {
        "分类": [a, b, c, d, e, f, g, h, i, j, k],
         "数据": [l, m, n, o, p, q, r,s,t,u,v], }

    df = pd.DataFrame(data)
    plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
    plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题
    # plt.tight_layout()  # 解决绘图时上下标题重叠现象
    # plt.yticks(fontproperties='Times New Roman', size=15,weight='bold')#设置大小及加粗
    fig, ax = plt.subplots(figsize=(3, 4))
    ax.axis("off")
    ax.axis("tight")
    ax.set_title(Labe,fontsize=20,loc='center',color='blue')  # 设置一个标题头
    tb = ax.table(cellText=df.values,colLabels=df.columns, bbox=[0, 0, 1, 1], )
    tb[0, 0].set_facecolor("lightblue")
    tb[0, 1].set_facecolor("lightblue")
    tb[0, 0].set_text_props(color="black")
    tb[0, 1].set_text_props(color="black")

plt.show()  # 展示图片
# plt.savefig('C:/你的/文件/保存/地址/name.png',dpi = 170)  # 保存图片


