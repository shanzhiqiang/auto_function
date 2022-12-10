import time
import json
from logging.handlers import TimedRotatingFileHandler

from utils import DriverUtil
import logging

#定义获取登陆失败的弹窗信息
def get_tips_info():
    time.sleep(5)
    msg = DriverUtil.get_driver().find_element_by_class_name('layui-layer-content').text
    return msg

#定义读取测试数据的方法
def get_data(filename):
    result = []
    with open('../data/'+filename,encoding='utf8') as f:
        data = json.load(f)
        for value in data.values():
            result.append((value.values()))
        return result

#打印日志
def get_log():
    # 创建日志器
    mylogger = logging.getLogger()
    # 创建处理器
    shl = logging.StreamHandler()
    thl = TimedRotatingFileHandler('../log/{}.log'.format(time.strftime('%y%m%d%H%M%S')),
                                   when='h', interval=1, backupCount=0)
    # 创建格式化器
    fmt = logging.Formatter()
    # 处理器添加格式化器
    shl.setFormatter(fmt)
    thl.setFormatter(fmt)
    # 日志器添加处理器
    mylogger.addHandler(shl)
    mylogger.addHandler(thl)
    # 日志器设置日志级别
    mylogger.setLevel('INFO')