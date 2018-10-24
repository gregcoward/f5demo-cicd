#!/usr/bin/python

import sys
import requests
import socket
import json

pubAddr = sys.argv[1] + '.northeurope.azurecontainer.io'
poolIP = socket.gethostbyname(pubAddr)

url = 'https://10.23.0.74/mgmt/cm/global/tasks/apply-template'

data1 = '''{
    "configSetName": "'''
data1h = '''",
    "domains": [
        {
            "domainName": "'''
data1h1 = '''"
        }
    ],
    "defaultDeviceReference": {
        "link": "https://localhost/mgmt/shared/resolver/device-groups/cm-adccore-allbigipDevices/devices/'''
data1h2 = '''"
    },
    "resources": {
        "ltm:virtual:7a5f7da91996": [
            {
                "parameters": {
                    "name": "default_vs_443",
                    "destinationAddress": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "destinationPort": "443"
                },
                "parametersToRemove": [],
                "subcollectionResources": {
                    "profiles:66720e074586": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ],
                    "profiles:9448fe71611e": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ],
                    "profiles:194b8588f24f": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ],
                    "profiles:359c36b6d854": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ]
                }
            }
        ],
        "ltm:virtual:40e8c4a6f542": [
            {
                "parameters": {
                    "name": "default_redirect_vs_80",
                    "destinationAddress": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "destinationPort": "80"
                },
                "parametersToRemove": [],
                "subcollectionResources": {
                    "profiles:9448fe71611e": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ],
                    "profiles:194b8588f24f": [
                        {
                            "parameters": {},
                            "parametersToRemove": []
                        }
                    ]
                }
            }
        ],
        "ltm:node:ec43f2b8cf6e": [
            {
                "parameters": {
                    "name": "'''
data2 = '''",
                    "address": "'''
data3 = '''"
                },
                "parametersToRemove": []
            }
        ],
        "ltm:pool:be70d46c6d73": [
            {
                "parameters": {
                    "name": "pool_0"
                },
                "parametersToRemove": [],
                "subcollectionResources": {
                    "members:240804b1705c": [
                        {
                            "parameters": {
                                "port": 80,
                                "nodeReference": {
                                    "link": "#/resources/ltm:node:ec43f2b8cf6e/'''
data4 = '''",
                                    "fullPath": "# '''
data5 = '''"
                                }
                            },
                            "parametersToRemove": []
                        }
                    ]
                }
            }
        ],
        "ltm:monitor:http:fd07629373b0": [
            {
                "parameters": {
                    "name": "monitor-http"
                },
                "parametersToRemove": []
            }
        ],
        "ltm:profile:client-ssl:14c995c33411": [
            {
                "parameters": {
                    "name": "clientssl",
                    "certKeyChain": [
                        {
                            "name": "f5demowild19",
                            "certReference": {
                                "id": "df4a3c41-2c27-3840-bd7a-0baa46b474a7",
                                "name": "f5demowild19.crt",
                                "kind": "cm:adc-core:working-config:sys:file:ssl-cert:adcsslcertstate",
                                "partition": "Common",
                                "link": "https://localhost/mgmt/cm/adc-core/working-config/sys/file/ssl-cert/df4a3c41-2c27-3840-bd7a-0baa46b474a7",
                                "fullPath": "/Common/f5demowild19.crt"
                            },
                            "keyReference": {
                                "id": "0a8d2bc2-af51-3253-bc96-016dca8eaadd",
                                "name": "f5demowild19.key",
                                "kind": "cm:adc-core:working-config:sys:file:ssl-key:adcsslkeystate",
                                "partition": "Common",
                                "link": "https://localhost/mgmt/cm/adc-core/working-config/sys/file/ssl-key/0a8d2bc2-af51-3253-bc96-016dca8eaadd",
                                "fullPath": "/Common/f5demowild19.key"
                            }
                        }
                    ]
                },
                "parametersToRemove": []
            }
        ],
        "ltm:profile:http:8ba4bb101701": [
            {
                "parameters": {
                    "name": "profile_http"
                },
                "parametersToRemove": []
            }
        ]
    },
    "addAnalytics": true,
    "subPath": "'''
data6 = '''",
    "templateReference": {
        "link": "https://localhost/mgmt/cm/global/templates/b165c7f0-749f-31e7-88df-16b11e6690d8"
    },
    "mode": "CREATE"
}'''

databuild = data1 + sys.argv[2] + data1h + sys.argv[2] + data1h1 + sys.argv[3] + data1h2 + poolIP + data2 + poolIP + data3 + poolIP + data4 + poolIP + data5 + sys.argv[2] + data6
response =  requests.post(url, data=databuild, verify=False, auth=('admin', 'F5testnet'))
