# python project final format

#!/usr/bin/env python3
import json
import os
import requests
import io
path = os.listdir('/data/feedback')
for file in path:
    text = open('/data/feedback/'+file,'r', encoding='utf8')
    data = text.readlines()
    print("parsing file and placing into dictionary")
    dic = {"title": data[0], "name":data[1], "date":data[2], "feedback":data[3:]}
    # its turning it into a dictionary of lists
    # json_objest = json.dumps(dic, indent = 2)
    print("sending post request to web via json")
    test = requests.get('http://34.67.91.127/feedback/')
    status_test = test.status_code
    print(status_test)
    response = requests.post("http://34.67.91.127/feedback/", data = dic)
    status = response.status_code
    print(status)
    text.close
