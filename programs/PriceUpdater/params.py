# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 10:35:39 2017

@author: woon.zhenhao
"""

import urllib
from hashlib import sha256
from hmac import HMAC
from datetime import datetime
import pytz

#Get UTC time in isoformat
local = pytz.timezone ("Singapore")
local_dt = local.localize(datetime.now(), is_dst=None)
utc_dt = local_dt.astimezone (pytz.utc)
dt=utc_dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")

apiKeys=['RL7K4yrxUUt5hvTCrsrdCzX-IyMHHy8voUw4L1PEa0ovLwN5dP_HHNwI']
userId=['woonzh@hotmail.com']
name=['test']

def getUserList():
    size = len(name)
    sen='---------------------------------------\n'
    for i in range(0,size):
        if i > 0:
            sen+='\n'
        sen= sen + str(i+1)+') ' +str(name[i])
    return sen

def checkAccuracy(choice):
    try:
        choice=int(choice)
    except ValueError:
        return False
    
    if choice in range(0+1,len(name)+1):
        return True
    else:
        return False

def queryStorer():
    sen=getUserList()
    cor = False
    storer=0
    
    while cor==False:
        print(sen)
        storer = input("Please Choose id of storer (e.g. 1): ")
        cor=checkAccuracy(storer)
        if cor==False:
            print("Please choose a valid number\n")
        else:
            confirm=input("Confirm update price list to " + name[int(storer)-1]+" ? (y/n): ")
            if confirm!='y' and confirm!='Y':
                cor=False

    return int(storer)-1
    
def getParams():
    index=queryStorer()
    
    param={
        'Version': '1.0',
        'Action': 'UpdatePriceQuantity',
        'Format':'JSON',
        'Timestamp': dt}
    param['UserID']=userId[index]
    
    api_key=apiKeys[index]
    
    concatenated = urllib.parse.urlencode(sorted(param.items()))
    
    sig=HMAC(bytearray(api_key,'ASCII'), bytearray(concatenated, 'ASCII'), sha256).hexdigest()
    param['Signature'] = sig
    
    return param
    