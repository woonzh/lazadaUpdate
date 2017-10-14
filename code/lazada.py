# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 09:29:25 2017

@author: woon.zhenhao
"""

import requests
import pandas as pd
import urllib
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import json
import pytz
import xml.etree.cElementTree as ET

#Get UTC time in isoformat
local = pytz.timezone ("Singapore")
local_dt = local.localize(datetime.now(), is_dst=None)
utc_dt = local_dt.astimezone (pytz.utc)
dt=utc_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")

apiKeys=['RL7K4yrxUUt5hvTCrsrdCzX-IyMHHy8voUw4L1PEa0ovLwN5dP_HHNwI']
userId=['woonzh@hotmail.com']
name=['test']

#nameChoice=raw_input("Please choose storer"+)

#populating params
param={
        'UserID':'woonzh@hotmail.com',
        'Version': '1.0',
        'Action': 'UpdatePriceQuantity',
        'Format':'JSON',
        'Timestamp': dt}
api_key= 'RL7K4yrxUUt5hvTCrsrdCzX-IyMHHy8voUw4L1PEa0ovLwN5dP_HHNwI'
concatenated = urllib.parse.urlencode(sorted(param.items()))
sig=HMAC(bytearray(api_key,'ASCII'), bytearray(concatenated, 'ASCII'), sha256).hexdigest()
param['Signature'] = sig

#API URL
getProdUrl = 'https://api.sellercenter.lazada.sg'

#Deriving xml from csv
root = ET.Element("Request")
root2 = ET.SubElement(root, "Product")
root3 = ET.SubElement(root2, "Skus")
df=pd.read_csv('source.csv')
fields=['SellerSku','Price','SalePrice','SaleStartDate','SaleEndDate']

for i in df.index:
    root4=ET.SubElement(root3,"Sku")
    for j in range(0,len(fields)):
        data=df.iloc[i,j]
        if df.iloc[i,j] == df.iloc[i,j]:
            if j>2:
                ET.SubElement(root4,fields[j],).text=datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(data) - 2).strftime("%Y-%m-%d")
            else:
                ET.SubElement(root4,fields[j],).text=str(data)
        else:
            ET.SubElement(root4,fields[j],).text=''
        
tree = ET.ElementTree(root)
tree.write('prices.xml')

#Sending xml to API
response=requests.post(getProdUrl,params=param, data=open('prices.xml').read())
if (response.status_code)==200:
    df=json.loads(response.content.decode('utf-8'))
    print(df)
else:
    df='API Failed'
