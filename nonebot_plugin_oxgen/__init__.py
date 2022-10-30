import asyncio
import os
from PIL import Image, ImageDraw, ImageFont

from nonebot import on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot_plugin_guild_patch import GuildMessageEvent, MessageSegment

import requests  # 导入requests库
from lxml import etree  # 倒入lxml 库(没有这个库，pip install lxml安装)
from bs4 import BeautifulSoup

img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'

# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)


wiki = on_command("wiki", rule=to_me(), aliases={"查", "查找"}, priority=5)


@wiki.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/wiki 铝，则args为铝
    if plain_text:
        matcher.set_arg("wiki_", args)  # 如果用户发送了参数则直接赋值


@wiki.got("wiki_", prompt="你想查询哪个元素文本呢？")
async def handle_city(wiki_: Message = Arg(), wiki_name: str = ArgPlainText("wiki_")):
    # if wiki_name not in ["铁", "铝"]:  # 这里举个铁和铝的例子，如果参数不符合要求，则提示用户重新输入
    # 可以使用平台的 Message 类直接构造模板消息
    # await wiki.reject(wiki_.template("你想查询的元素 {wiki_} 暂不支持，请重新输入！"))

    wiki_name_text = await get_weather(wiki_name)
    # await wiki.finish(wiki_name_text)
    await get_name_img(wiki_name_text)
    await wiki.send(send_img('comments.png'))





# 在这里编写获取元素文本信息的函数
async def get_weather(city_name: str) -> str:
    url = 'https://oxygennotincluded.fandom.com/zh/wiki/%E5%85%83%E7%B4%A0'  # 请求地址缺氧wiki里的元素类

    Subpage = requests.get(url)  # 拼接后的url
    html = etree.HTML(Subpage.text)

    def href_page_text():
        href_ = html.xpath(
            '//*[@id="mw-content-text"]/div/table/tbody/tr/td/table/tbody/tr/td/div/span/a[@title="名"]'.replace("名", f"{city_name}"))
        for href_a in href_:
            href_b = href_a.xpath('./@href')[0]
            get_url_tow = 'https://oxygennotincluded.fandom.com'  # url拼接
            href_Subpage_ = get_url_tow + href_b  # 调取href下的链接并拼接url
            href_Subpage = requests.get(href_Subpage_)
            href_Subpage_text = href_Subpage.text
            # print(href_Subpage)

            return href_Subpage_text

    href_page_text = href_page_text()
    await asyncio.sleep(5)

    def massage_txt():
        # 把源码交给bs
        main_page_see = BeautifulSoup(href_page_text, "html.parser")
        # 找到描述文本
        meat_txt = main_page_see.find("meta", {"property": "og:description"}).get("content")
        return meat_txt

    a_text = massage_txt()
    return a_text


# 得到文字制作含文字的图片
async def get_name_img(city_name_img: str):
    LINE_CHAR_COUNT = 18 * 2  # 每行字符数：30个中文字符(=60英文字符)
    CHAR_SIZE = 50
    TABLE_WIDTH = 4

    def line_break(line):
        ret = ''
        width = 0
        for c in line:
            if len(c.encode('utf8')) == 3:  # 中文
                if LINE_CHAR_COUNT == width + 1:  # 剩余位置不够一个汉字
                    width = 2
                    ret += '\n' + c
                else:  # 中文宽度加2，注意换行边界
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

    output_str = city_name_img  # 测试字符串
    output_str = line_break(output_str)
    d_font = ImageFont.truetype('C:/Windows/Fonts/simsun.ttc', CHAR_SIZE)
    lines = output_str.count('\n')  # 计算行数

    image = Image.new("L", (LINE_CHAR_COUNT * CHAR_SIZE // 2, CHAR_SIZE * lines), "white")
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text=output_str, fill='#000000', font=d_font, spacing=4)  # spacing调节机制不清楚如何计算

    # image.show()  # 直接显示图片
    image.save('J:/Github/nonebot2/nb2/src/plugins/nonebot_plugin_oxgen/img/comments.png', 'PNG')  # 保存在当前路径下，格式为PNG
    image.close()
