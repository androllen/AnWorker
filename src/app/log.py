# http://www.debugger.wiki/article/html/1562592270692275
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Time: 2019/12/30 10:59:50
# Contact: androllen#hotmail.com
import os
import logging
from logging import handlers


class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }

    def __init__(
        self,
        level='info',
        when='D',
        backCount=3,
        fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
    ):
        _ndir = os.path.join(os.getcwd(), 'logs')
        _filename = os.path.join(_ndir, 'all.log')
        if not os.path.exists(_ndir):
            os.makedirs(_ndir)

        self.logger = logging.getLogger(_filename)
        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 设置日志级别

        # 往文件里写入
        # 指定间隔时间自动生成文件的处理器
        timed_rotating_file_handler = handlers.TimedRotatingFileHandler(
            filename=_filename,
            when=when,
            backupCount=backCount,
            encoding='utf-8')

        # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        timed_rotating_file_handler.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(timed_rotating_file_handler)

        # 往屏幕上输出
        # stream_handler = logging.StreamHandler()
        # stream_handler.setFormatter(format_str)
        # self.logger.addHandler(stream_handler)
