import json

import requests  # 倒入requests库
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)
from bs4 import BeautifulSoup


# 获取用户要查询的元素内容 然后传入到下面的函数当中
def href_page_text(href):  # 元素子内容
    Subpage = requests.get(href)  # 拼接后的url
    Subpage_text = Subpage.text
    # 把源码交给bs
    main_page_two = BeautifulSoup(Subpage_text, "html.parser")
    # 找到table下的所有a标签
    div_tow = main_page_two.find("table", {"class": "navbox-section"}).find_all("a", title="钢")
    # print(div_tow)
    for ii in div_tow:
        get_url_tow = 'https://oxygennotincluded.fandom.com'  # url拼接
        href_Subpage = get_url_tow + ii.get("href", )  # 调取href下的链接并拼接url

        href_Subpage = requests.get(href_Subpage)
        href_Subpage_text = href_Subpage.text
        return href_Subpage_text


# 拿到元素内容文本
def massage_txt(href):
    # 把源码交给bs
    main_page_see = BeautifulSoup(href, "html.parser")
    # 找到描述文本
    meat_txt = main_page_see.find("meta", {"property": "og:description"}).get("content")
    return meat_txt


# 拿到元素内容文本详细
def massage_zu(href):
    main_page_see = BeautifulSoup(href, "html.parser")
    meat_txt = main_page_see.find("aside", {"role": "region"})
    wb_data = meat_txt.text
    send = wb_data.rstrip()

    return send


from PIL import Image, ImageFont, ImageDraw  # 引入图片，画图笔，图片字体三个库


def CreateImg(text):
    fontSize = 30
    liens = text.split('\n')
    # 画布颜色
    im = Image.new("RGB", (480, len(liens) * (fontSize + 5)), (245, 255, 250))  # 建一张新图，颜色用RGB，尺寸 750x2000，底色三个255表示纯白
    dr = ImageDraw.Draw(im)
    # 字体样式，文章结尾我会放上连接
    fontPath = r"C:\Windows\Fonts\STKAITI.TTF"

    font = ImageFont.truetype(fontPath, fontSize)
    # 文字颜色
    dr.text((0, 0), text, font=font, fill="#0f0f0f")
    im.save('J:/Github/nonebot2/nb2/src/plugins/group_text1/img/output.png')
    # im.show()
