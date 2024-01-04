# -*- coding: utf-8 -*-

from garbevents.sensors_backstage_event import GetData

from garbevents.settings import Settings as ST

'mitmdump -p 8889 -s test_sensors_backstage_events.py'

ST.url = 'https://sc.jiligaga.com/sa?project=default'
ST.report_path = 'report'
ST.all_events = ['phone_message_send_tech']
ST.events_properties = {
    'phone_message_send_tech': ['source', 'msgid']
}
GetData.backstage('server_ip', 'server_name', 'server_password')

addons = [
    GetData()
]
