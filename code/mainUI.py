# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:52:21 2017

@author: woon.zhenhao
"""

import priceUpdate as PU
import orderUpdate as OU

options=['Update Pricing and promotions','Update orders']

def optionsList():
    size = len(options)
    sen='---------------------------------------\n'
    for i in range(0,size):
        if i > 0:
            sen+='\n'
        sen= sen + str(i+1)+') ' +str(options[i])
    return sen

def checkAccuracy(choice):
    try:
        choice=int(choice)
    except ValueError:
        return False
    
    if choice in range(0+1,len(options)+1):
        return True
    else:
        return False
    
def queryChoice():
    sen=optionsList()
    cor = False
    choice=0
    
    while cor==False:
        print(sen)
        choice = input("Please Choose id of choice (e.g. 1): ")
        cor=checkAccuracy(choice)
        if cor==False:
            print("Please choose a valid number\n")

    return int(choice)-1

choice=queryChoice()
if choice==0:
    PU.execute()
if choice==1:
    OU.execute()