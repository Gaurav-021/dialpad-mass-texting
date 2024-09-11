import csv
import requests
import time
import os
import yaml

with open('data.yml', 'r') as file:
    yamlData = yaml.safe_load(file)

with open('phone.csv', newline='') as f:
    reader = csv.reader(f)
    array = list(reader)
x = -1
for y in range(len(array)):
    time.sleep(0.75)    
    x +=1
    print(x)

    print(array[x])
    print(len(array))

    url = yamlData['url']
    payload = {
        "infer_country_code": False,
        "sender_group_type": "office",
        "sender_group_id": yamlData['sender_group_id'],
        "text": yamlData['text'],
        "user_id": yamlData['user_id'],
        "to_numbers": array[x] 
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)

    print(response.text)
    
        

        