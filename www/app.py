#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Date    : 2016-08-25 15:37:15
# @Author  : 青峰
# @Desc    : web application骨架

import logging

# 设置日志等级,默认为WARNING.只有指定级别或更高级的才会被追踪记录
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(message)s",  # display date
                    datefmt="[%Y-%m-%d %H:%M:%S]")

# asyncio的编程模型就是一个消息循环
import asyncio
import os
import json
import time
from datetime import datetime

from aiohttp import web

# handler:处理url请求,并返回响应结果


def index(request):
    # 默认以bytes形式返回响应结果,设置类型为HTML文本
    return web.Response(body=bytes('<h1>Awesome By 青峰</h1>', encoding='utf-8'),
                        headers={'Content-Type': 'text/html;charset=utf-8'})

# 初始化


@asyncio.coroutine  # 把一个generator标记为coroutine类型
def init(loop):
    # 创建web应用
    app = web.Application(loop=loop)
    # arg1:捕获请求方式,arg2:根据指定的前缀匹配url,arg3:handler
    app.router.add_route('GET', '/', index)
    # 调用子协程:创建一个TCP服务器,绑定到"127.0.0.1:9000"socket,并返回一个服务器对象
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # 记录日志
    logging.info('server started at http://127.0.0.1:9000...')
    # 返回服务器对象
    return srv

# loop是一个消息循环对象
loop = asyncio.get_event_loop()
# 在消息循环中执行协程-coroutine
loop.run_until_complete(init(loop))
# 消息循环一直执行
loop.run_forever()
