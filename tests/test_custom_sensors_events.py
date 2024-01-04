# -*- coding: utf-8 -*-
from garbevents.custom_sensors_events import GetData

from garbevents.settings import Settings as ST

import pandas as pd

'mitmdump -p 8889 -s test_custom_sensors_events.py'

#  国内版本
ST.url = 'https://sc.jiliguala.com/sa?project=default'
#  ST.url = 'https://sc.jiliguala.com/sa?project=production'

#  海外版本
# ST.url = 'https://sc.jiligaga.com/sa?project=default'
#  ST.url = 'https://sc.jiligaga.com/sa?project=production'


ST.report_path = 'report'


ST.all_events = ['sublesson_exit_true_click']
ST.events_properties = {
    'sublesson_exit_true_click': ['_from', 'sublesson_id', 'sublesson_name']
}

# 提取excel中的数据,并转换成 '':[]的格式
# def excel_to_dict():
#     df = pd.read_excel('/Users/jlglqa/Downloads/叽里呱啦核心埋点.xlsx', sheet_name=1, header=1, usecols='A, B',
#                        keep_default_na=False, dtype=str)
#
#     df_li = df.values.tolist()  # 转换成list
#
#     ST.all_events = []
#     for s_li in df_li:
#         ST.all_events.append(s_li[0])  # 存储所有的事件名称
#     ST.all_events = list(set(ST.all_events))  # 去重
#
#     ST.events_properties = {}
#     for s in ST.all_events:
#         ST.events_properties[s] = []  # 初始化每个事件的属性
#
#     for s_li in df_li:
#         ST.events_properties[s_li[0]].append(s_li[1])  # 存储每个事件的属性
#
#     print(ST.events_properties)


addons = [
    GetData(),
    # excel_to_dict()
]
