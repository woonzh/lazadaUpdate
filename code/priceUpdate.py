# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:45:04 2017

@author: woon.zhenhao
"""

import requests
import json
import params 
import xmlGenerator
import os

def checkRepeat():
    cont=input('Would like to try again? (y/n):')
    if cont=='y' or cont=='Y':
        return True
    else:
        return False
    
def execute():
    cont=True
    
    while cont:
        #Get param
        param = params.getParams()
        
        #API URL
        getProdUrl = 'https://api.sellercenter.lazada.sg'
        
        #Deriving xml from csv
        sourceFile='source.xlsx'
        outputFile='price.xml'
        xmlCor=xmlGenerator.getPriceUpdateXML(sourceFile,outputFile)
        
        if xmlCor:
            #Sending xml to API
            response=requests.post(getProdUrl,params=param, data=open(outputFile).read())
            if (response.status_code)==200:
                df=json.loads(response.content.decode('utf-8'))
                if list(df)==['SuccessResponse']:
                    print('Success')
                    cont=False
                else:
                    print(df)
                    cont = checkRepeat()
            else:
                print('Connection failed')
                cont=checkRepeat()
        else:
            print('Error in xml file. Please ensure all your SKU and normal price is filled.')
            cont=checkRepeat()
        
    os.system('pause')
    
