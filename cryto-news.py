import requests
import sys
import json
from columnar import columnar
from click import style

parameters = {"data":"feeds","key":"rks643epq9onrriknr62w","symbol":"DOGE","limit":"10","sources":"twitter"}
r = requests.get("https://api.lunarcrush.com/v2", params=parameters)

if r.status_code != 200:
    print("Connection not successful")
    sys.exit()

json_response = r.json()
for data in json_response.keys():
    if data == "data":
        value = list(json_response.values())
list_of_dictionary_data = value[2]

data_list = []
for influencer_data in list_of_dictionary_data:
    data_data = []
    for data in influencer_data.keys(): 
        if data == 'social_score':
            data_data.append(influencer_data[data])
        if data == 'display_name':
            data_data.append(influencer_data[data])
        if data == 'twitter_screen_name':
            data_data.append(influencer_data[data])
        if data == 'url':
            data_data.append(influencer_data[data])
        if data=='body':
            data_data.append(influencer_data[data])

    data_list.append(data_data)
headers = ["Influence","Tweet","Tweet URL","Name","Twitter Handle"]
table = columnar(data_list,headers)
print(table)