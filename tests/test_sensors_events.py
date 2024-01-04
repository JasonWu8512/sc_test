# -*- coding: utf-8 -*-

from garbevents.sensors_events import GetData

from garbevents.settings import Settings as ST

import pandas as pd

'mitmdump -p 8889 -s test_sensors_events.py'

#  国内版本
ST.url = 'https://sc.jiliguala.com/sa?project=default'


# ST.url = 'https://sc.jiliguala.com/sa?project=production'

#  从excel表格中读取埋点事件名
# def excel_one_line_to_list():
#     df = pd.read_excel('/Users/jlglqa/Downloads/叽里呱啦核心埋点.xlsx', sheet_name='埋点汇总', header=1, usecols='B, F',
#                        keep_default_na=False)
#
#     df_li = df.values.tolist()
#     ST.all_events = []
#     for s_li in df_li:
#         ST.all_events.append(s_li[0])
#
#     print(ST.all_events)


#  海外版本
# ST.url = 'https://sc.jiligaga.com/sa?project=default'
# ST.url = 'https://sc.jiligaga.com/sa?project=production'


# def excel_one_line_to_list_intl():
#     df = pd.read_excel('/Users/jlglqa/Downloads/cocos埋点大全.xlsx', sheet_name='埋点汇总', header=0, usecols='A',
#                        keep_default_na=False)
#
#     df_li = df.values.tolist()
#     ST.all_events = []
#     for s_li in df_li:
#         ST.all_events.append(s_li[0])
#
#     print(ST.all_events)

ST.report_path = 'report'
ST.all_events = ['cocos_video_caption_change_tech', 'sub_lesson_click']

addons = [
    GetData(),
    # excel_one_line_to_list(),
    # excel_one_line_to_list_intl(),
]
