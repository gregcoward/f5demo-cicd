#!/usr/bin/python

import sys
import requests
import json
import time

status = "NA"


url = 'https://172.16.60.74/mgmt/cm/global/tasks/apply-template'
data1 = '''{"configSetName":'''
data2 = ''', "mode": "DELETE"}'''
data3 = data1 + sys.argv[1] + data2

response = requests.post(url, data=data3, verify=False, auth=('admin', 'F5testnet'))
obj = response.json()
url2 = (url + '/' + obj['id'])
response2 = requests.get(url2, verify=False, auth=('admin', 'F5testnet'))
status = response2.json()['status']
print('First Status: '+ status)

while status != 'FINISHED' and status != 'FAILED':
    try:
        response2 = requests.get(url2, verify=False, auth=('admin', 'F5testnet'))
        status = response2.json()['status']
        time.sleep(5)
        print(status)
    except Exception as e:
        break

if status == 'FAILED':
    response = requests.post(url, data=data3, verify=False, auth=('admin', 'F5testnet'))
    obj = response.json()
    url2 = (url + '/' + obj['id'])
    response2 = requests.get(url2, verify=False, auth=('admin', 'F5testnet'))
    status = response2.json()['status']

print(status)
