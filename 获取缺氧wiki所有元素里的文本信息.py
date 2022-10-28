# coding=utf-8
import re
import requests
from urllib import request
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)
from bs4 import BeautifulSoup

from PIL import Image, ImageDraw, ImageFont


url = 'https://oxygennotincluded.fandom.com/zh/wiki/%E5%85%83%E7%B4%A0'  # 请求地址缺氧wiki里的元素类

Subpage = requests.get(url)  # 拼接后的url
html = etree.HTML(Subpage.text)


aww = input("请输入要查询的元素：")
def href_page_text():
    href_ = html.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td/table/tbody/tr/td/div/span/a[@title="名"]'.replace("名",f"{aww}"))
    for href_a in href_:
        href_b = href_a.xpath('./@href')[0]
        get_url_tow = 'https://oxygennotincluded.fandom.com'  # url拼接
        href_Subpage_ = get_url_tow + href_b  # 调取href下的链接并拼接url
        href_Subpage = requests.get(href_Subpage_)
        href_Subpage_text = href_Subpage.text
        # print(href_Subpage)

        return href_Subpage_text
href_page_text = href_page_text()


def massage_txt():
    
    main_page_see = BeautifulSoup(href_page_text, "html.parser")
    # 找到描述文本
    meat_txt = main_page_see.find("meta", {"property": "og:description"}).get("content")
    return meat_txt

mass_txt = massage_txt()




LINE_CHAR_COUNT = 50*2  # 每行字符数：30个中文字符(=60英文字符)
CHAR_SIZE = 30
TABLE_WIDTH = 4

def line_break(line):
    ret = ''
    width = 0
    for c in line:
        if len(c.encode('utf8')) == 3:  # 中文
            if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                width = 2
                ret += '\n' + c
            else: # 中文宽度加2，注意换行边界
                width += 2
                ret += c
        else:
            if c == '\t':
                space_c = TABLE_WIDTH - width % TABLE_WIDTH  # 已有长度对TABLE_WIDTH取余
                ret += ' ' * space_c
                width += space_c
            elif c == '\n':
                width = 0
                ret += c
            else:
                width += 1
                ret += c
        if width >= LINE_CHAR_COUNT:
            ret += '\n'
            width = 0
    if ret.endswith('\n'):
        return ret
    return ret + '\n'


output_str = mass_txt  # 测试字符串
output_str = line_break(output_str)
d_font = ImageFont.truetype('C:/Windows/Fonts/simsun.ttc', CHAR_SIZE)
lines = output_str.count('\n')  # 计算行数

image = Image.new("L", (LINE_CHAR_COUNT*CHAR_SIZE // 2, CHAR_SIZE*lines), "white")
draw_table = ImageDraw.Draw(im=image)
draw_table.text(xy=(0, 0), text=output_str, fill='#000000', font= d_font, spacing=4)  # spacing调节机制不清楚如何计算

image.show()  # 直接显示图片
# image.save('comments.png', 'PNG')  # 保存在当前路径下，格式为PNG
image.close()

