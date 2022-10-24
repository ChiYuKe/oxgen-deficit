from .data import get_nan
from .dataname import href_page_text, massage_txt, massage_zu, CreateImg

import os

import asyncio

from nonebot import on_command, Bot
from nonebot_plugin_guild_patch import GuildMessageEvent, Message, MessageSegment
from nonebot.params import ArgPlainText, CommandArg
from nonebot.matcher import Matcher


img_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'
# 发送图片时用到的函数, 返回发送图片所用的编码字符串
def send_img(img_name):
    global img_path
    return MessageSegment.image(img_path + img_name)

wiki = on_command('wiki')


@wiki.handle()
async def _handle(matcher: Matcher, name_: Message = CommandArg()):
    name_str = str(name_)  # 把Any变成字符串类型
    if name_str == "教程":
        name_str = 0
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "复制人":
        name_str = 1
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "建筑":
        name_str = 2
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "小动物":
        name_str = 3
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "技能":
        name_str = 4
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "装备":
        name_str = 5
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "元素":
        name_str = 6
        na = get_nan(name_str)  # 得到链接给nb
        await asyncio.sleep(2)
        # await wiki.send(str(na))
        nb = href_page_text(na)  # 得到链接给nc
        await asyncio.sleep(1)
        nc = massage_txt(nb)
        await asyncio.sleep(1)
        nd = massage_zu(nb)
        await asyncio.sleep(1)
        ne = CreateImg(nd)
        # await wiki.send(str(nc))
        # await wiki.send(str(nd))
        await wiki.send(send_img('output.png'))

    elif name_str == "食物":
        name_str = 7
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "间歇泉":
        name_str = 8
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "植物":
        name_str = 9
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "研究":
        name_str = 10
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "生态":
        name_str = 11
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "小行星":
        name_str = 12
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "眼冒金星":
        name_str = 13
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "火箭":
        name_str = 14
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    elif name_str == "小行星群":
        name_str = 15
        na = get_nan(name_str)
        await asyncio.sleep(2)
        await wiki.send(str(na))
    else:
        await wiki.send("没有您想要的哦~目前只有以下这十六大类")
        await wiki.send("教程，复制人，建筑，小动物，技能，装备，元素，食物，间歇泉，植物，研究，生态，小行星，眼冒金星，火箭，小行星群")

    # name_int = int(name_str)  #把字符串变成数字类型

    # await wiki.send(name_)
    # na = get_nan(name_int)
    # await wiki.send("正在查询.....")
    # await asyncio.sleep(3)
    # await wiki.send("完成")
    # await wiki.send(str(na))
    # await on_command('wiki').send(message=aa['name'] + ':' + aa['href'])
