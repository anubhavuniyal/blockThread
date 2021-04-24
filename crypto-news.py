#!/usr/bin/python3
import requests
import argparse
import sys
import json
import matplotlib.pyplot as plt
from columnar import columnar
from datetime import date
from datetime import timedelta

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-d","--data",choices=["feeds","influencers","influencer","price-ticker"],help="Choose the type of data you want to see",default="price-ticker")
group.add_argument("--coinoftheday",help="Display information about the current coin of the day",action="store_true")
parser.add_argument("-k","--key",help="Your lunar api key")
parser.add_argument("-s","--symbol",help="Details of a coin to display",default="BTC")
parser.add_argument("-l","--limit",help="Number of data to show",default=10)
parser.add_argument("--sources",choices=["twitter","reddit"],help="Sources to get the information from",default="twitter")
args = parser.parse_args()

data = args.data
key = args.key
symbol = args.symbol
limit = args.limit
sources=args.sources

if args.coinoftheday:
    parameters = {"data":"coinoftheday","key":key}
    r = requests.get("https://api.lunarcrush.com/v2",params=parameters)
    json_response = r.json()
    for data in json_response.keys():
        if data == "data":
            value = list(json_response.values())
    list_of_dictionary_data = value[2]
    print("Name\t\tSymbol")
    print(f"{list_of_dictionary_data['name']}\t\t{list_of_dictionary_data['symbol']}")
    sys.exit(0)

if data == "price-ticker":
    end = date.today()
    start = end - timedelta(days=30)
    r = requests.get(f"https://data.messari.io/api/v1/assets/{symbol}/metrics/price/time-series?start={start}&end={end}&interval=1d")
    json_response = r.json()


    for data in json_response.keys():
        if data == "data":
            value = list(json_response.values())
            dict_value = value[1]
            coin_value = dict_value['values']

    x = []
    o_y = []
    h_y = []
    l_y = []
    c_y = []
    day = 0

    for i in coin_value:
        o_y.append(i[1])
        h_y.append(i[2])
        l_y.append(i[3])
        c_y.append(i[4])
        x.append(day)
        day+=1

    plt.plot(x,o_y,label="Opening value")
    plt.plot(x,h_y,label="Highest value")
    plt.plot(x,l_y,label="Lowest value")
    plt.plot(x,c_y,label="Closing value")
    plt.legend()
    plt.xlabel(f"From {start} to {end}")
    plt.ylabel("Price changes")
    plt.title(f"{symbol} price ticker")
    plt.show()
    sys.exit(0)
 

parameters = {"data":data,"key":key,"symbol":symbol,"limit":limit,"sources":sources}

r = requests.get("https://api.lunarcrush.com/v2", params=parameters)

if r.status_code != 200:
    if r.status_code == 502:
        print("Invalid symbol entered")
    elif r.status_code == 401:
        print("API key invalid or expired")
    else:
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
        if data=='body' or data=='title':
            if sources == 'reddit':
                if data=='body':
                    pass
                else:
                    data_data.append(influencer_data[data])
            else:
                data_data.append(influencer_data[data])

    data_list.append(data_data)
if sources == 'twitter':
    headers = ["Influence","Tweet","Tweet URL","Name","Twitter Handle"]
else:
    headers = ["Influence","Title","Url"]
table = columnar(data_list,headers,no_borders=True)
print(table)
