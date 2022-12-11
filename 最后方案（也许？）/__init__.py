import asyncio
import os
import time
from typing import Dict

import requests

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Bot, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot_plugin_guild_patch import GuildMessageEvent, MessageSegment
import imgkit
from urllib.parse import quote

img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'


# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)


wiki = on_command("w", aliases={"/查", "/查找"}, priority=5)


@wiki.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/wiki 铝，则args为铝
    if plain_text:
        matcher.set_arg("wiki_", args)  # 如果用户发送了参数则直接赋值


@wiki.got("wiki_", prompt="你想查询哪个物品呢？")
async def handle_secondary_receive(wiki_: Message = Arg(), wiki_name: str = ArgPlainText("wiki_")):
    index = await get_index(wiki_name)
    if wiki_name not in index:  # 这里举个铁和铝的例子，如果参数不符合要求，则提示用户重新输入
        # 可以使用平台的 Message 类直接构造模板消息
        await wiki.finish("抱歉你要查找的不存在,你要找的可能是:" + index)
    basic_link = 'https://oxygennotincluded.fandom.com/zh/wiki/'
    text = quote(wiki_name, 'utf-8')  # 对中文进行编码
    after_splicing_link = basic_link + text  # url拼接
    await wiki.send("猫猫正在努力查找中....")
    await asyncio.sleep(1)
    try:
        await get_screenshot(after_splicing_link)
    except 0:
        pass
    time.sleep(1)
    await wiki.send(send_img('0_0.png'))
    # 检查指定的路径是否存在，如果存在，它将删除该路径对应的文件或目录
    path = r'C:\Users\29025\Desktop\Cat_Bot\mybot\src\plugins\nonebot_plugin_oxgen\img\0_0.png'
    if os.path.exists(path):
        os.remove(path)
    await wiki.finish("原文链接:" + "\n" + after_splicing_link)


async def get_index(key: str):
    url = f"https://oxygennotincluded.fandom.com/zh/api.php"
    data = {
        "action": "query",
        "list": "prefixsearch",
        "pssearch": key,
        "pslimit": "6",
        "format": "json"
    }
    resp = requests.get(url, params=data)
    resp_json = resp.json()
    index_name = resp_json['query']['prefixsearch']
    name0 = index_name[0]['title']
    name1 = index_name[1]['title']
    name2 = index_name[2]['title']
    name3 = index_name[3]['title']
    name4 = index_name[4]['title']
    name5 = index_name[5]['title']
    name_max = (name0 + "\n" + name1 + "\n" + name2 + "\n" + name3 + "\n" + name4 + "\n" + name5)
    return name_max


async def get_screenshot(web_links: str):
    url = web_links
    path_wk = r'C:\Users\29025\Desktop\Cat_Bot\mybot\src\plugins\nonebot_plugin_oxgen\wkhtmltopdf\bin\wkhtmltoimage.exe'
    config = imgkit.config(wkhtmltoimage=path_wk)
    picture_location = r'C:\Users\29025\Desktop\Cat_Bot\mybot\src\plugins\nonebot_plugin_oxgen\img\0_0.png'
    option = {
        'crop-w': 1100,  # 图片宽度
        'crop-h': 650,  # 图片长度
        'crop-x': 200,  # 与最左边的距离
        'crop-y': 1165,  # 与顶层的距离
        'encoding': 'UTF-8',
    }
    html2 = imgkit.from_url(url=url, config=config, options=option, output_path=picture_location)
