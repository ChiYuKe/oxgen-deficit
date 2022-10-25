import json
from webbrowser import get

import requests
import requests  # 倒入requests库
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)
from bs4 import BeautifulSoup





url = 'https://oxygennotincluded.fandom.com/zh/wiki/%E5%85%83%E7%B4%A0'  # 请求地址缺氧wiki里的元素类

Subpage = requests.get(url)  # 拼接后的url
Subpage_text = Subpage.text


def href_page_text() -> str:  # 元素子内容
    # 把源码交给bs
    main_page_two = BeautifulSoup(Subpage_text, "html.parser")
    # 找到span下的所有a标签
    div_tow = main_page_two.find("table", {"class": "navbox-section"}).find_all("a", title="铝") # 找到铝
    # print(div_tow)
    for ii in div_tow:
        get_url_tow = 'https://oxygennotincluded.fandom.com'  # url拼接
        href_Subpage = get_url_tow + ii.get("href", )  # 调取href下的链接并拼接url

        href_Subpage = requests.get(href_Subpage)
        href_Subpage_text = href_Subpage.text
        return href_Subpage_text


href_page_text = href_page_text()  # 发送获取到的页面源代码


# print(href_page_text)

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



# 拿到各个分类名称
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



# 拿到各个分类里面的数据
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
    ax.set_title(Labe,fontsize=10,loc='center',color='blue')
    tb = ax.table(cellText=df.values, colLabels=df.columns, bbox=[0, 0, 1, 1], )
    tb[0, 0].set_facecolor("lightblue")
    tb[0, 1].set_facecolor("lightblue")
    tb[0, 0].set_text_props(color="black")
    tb[0, 1].set_text_props(color="black")

# plt.show()
#保存图片
plt.savefig('C:/Users/liuke/Desktop/爬虫/FigA.png',dpi = 160)










# def massage_tag():
#     main_page_see = BeautifulSoup(href_page_text, 'lxml')
#     meat_guangxis = (main_page_see.select("aside div h3")[3].text)# 导热率
#     return meat_guangxis

# acsa = massage_tag()
# print(acsa)










# from PIL import Image, ImageFont, ImageDraw   # 引入图片，画图笔，图片字体三个库
 
 
# def CreateImg(text):
#     fontSize = 30
#     liens = text.split('\n')
#     #画布颜色
#     im = Image.new("RGB", (480, len(liens)*(fontSize+5)), (245,255,250))  # 建一张新图，颜色用RGB，尺寸 750x2000，底色三个255表示纯白
#     dr = ImageDraw.Draw(im)
#     #字体样式，文章结尾我会放上连接
#     fontPath = r"C:\Windows\Fonts\STKAITI.TTF"
    
#     font = ImageFont.truetype(fontPath, fontSize)
#     #文字颜色
#     dr.text((0, 0), text, font=font, fill="#0f0f0f")
#     # im.save('output.png')
#     im.show()
 
 
# CreateImg(massage_txt())
# CreateImg(massage_tag())





# import pygame

# #pygame初始化
# pygame.init()

# # 待转换文字
# text = massage_tag()

# #设置字体和字号
# font = pygame.font.SysFont('Microsoft YaHei', 64)

# #渲染图片，设置背景颜色和字体样式,前面的颜色是字体颜色
# ftext = font.render(text, True, (65, 83, 130),(255, 255, 255))

# #保存图片
# pygame.image.save(ftext, "image.jpg")#图片保存地址