import requests
import re
import time
from QcloudApi.qcloudapi import QcloudApi
import json


def get_out_ip():

    headers = {
        'Authorization': 'Basic YWRtaW46emhhbmd5YW5nMTIz',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
        'Referer': 'http://192.168.3.1/device-map/internet.asp',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
    }

    response = requests.get(
        'http://192.168.3.1/status_wanlink.asp', headers=headers, verify=False)

    response.encoding = 'utf-8'
    string_lst = response.text.split('\n')
    for txt in string_lst:
        if 'function wanlink_ip4_wan()' in txt:
            result = re.findall(
                r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", txt)
            return result[0]


def get_domain_id(ip):
    module = 'cns'

    # 对应接口的接口名，请参考wiki文档上对应接口的接口名
    action = 'RecordList'

    # 云API的公共参数
    config = {
        'secretId': 'AKIDd8VhlerEsW1MWUPvsiolX7XmfQ2ylcFg',
        'secretKey': "OalqkRySozznPp6RhmhQzMn8IG2c1EF4",
        'method': 'GET',
        'SignatureMethod': 'HmacSHA1',
        # 只有cvm需要填写version，其他产品不需要

    }

    # 接口参数，根据实际情况填写，支持json
    # 例如数组可以 "ArrayExample": ["1","2","3"]
    # 例如字典可以 "DictExample": {"key1": "value1", "key2": "values2"}
    action_params = {
        'domain': 'wdbefore.com',
    }

    try:
        service = QcloudApi(module, config)

        # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/Region/method/SignatureMethod参数
        # 重新设置请求的Region
        # service.setRegion('ap-shanghai')

        # 打印生成的请求URL，不发起请求
        print(service.generateUrl(action, action_params))
    # 调用接口，发起请求，并打印返回结果
        data = service.call(action, action_params)
    except Exception as e:
        import traceback
        print('traceback.format_exc():\n%s' % traceback.format_exc())
    data = json.loads(data)

    # 处理json 读记录ID Type Value

    records = data['data']['records']

    print(json.dumps(records, sort_keys=True, indent=4))
    for record in records:
        id_lst = []
        if record['type'] == 'A' and record['name'] == 'home':
            action = 'RecordModify'
            # 例如字典可以 "DictExample": {"key1": "value1", "key2": "values2"}
            action_params = {
                'domain': 'wdbefore.com',
                'subDomain': 'home',
                'recordId': record['id'],
                'recordType': 'A',
                'recordLine': '默认',
                'value': ip

            }

            try:
                service = QcloudApi(module, config)

                # 请求前可以通过下面几个方法重新设置请求的secretId/secretKey/Region/method/SignatureMethod参数
                # 重新设置请求的Region
                # service.setRegion('ap-shanghai')

                # 打印生成的请求URL，不发起请求
                print(service.generateUrl(action, action_params))
                # 调用接口，发起请求，并打印返回结果
                data = service.call(action, action_params)
            except Exception as e:
                print('traceback.format_exc():\n%s' %
                      traceback.format_exc())


ip_tmp = ''
while(True):
    ip_now = get_out_ip()

    if ip_now != '' and ip_now != ip_tmp:
        ip_tmp = ip_now
        get_domain_id(ip_now)

    print(ip_now)
    with open('ip.txt', 'w+') as f:
        f.write(str(ip_now))
    print('等待')
    time.sleep(10)
