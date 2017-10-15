# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:49:50 2017

@author: woon.zhenhao
"""

import pandas as pd
import xml.etree.cElementTree as ET
from datetime import datetime
import xlrd

root = ET.Element("Request")
root2 = ET.SubElement(root, "Product")
root3 = ET.SubElement(root2, "Skus")
fields=['SellerSku','Price','SalePrice','SaleStartDate','SaleEndDate']

def getPriceUpdateXML(sourceFile, outputFile):
    root = ET.Element("Request")
    root2 = ET.SubElement(root, "Product")
    root3 = ET.SubElement(root2, "Skus")
    fields=['SellerSku','Price','SalePrice','SaleStartDate','SaleEndDate']
    df2=xlrd.open_workbook(sourceFile)
    df2=df2.sheet_by_index(0)
    for i in range(1,df2.nrows):
        root4=ET.SubElement(root3,"Sku")
        for j in range(0,len(fields)):
            data=df2.cell_value(rowx=i, colx=j)
            if data!='':
                if j>2:
                    ET.SubElement(root4,fields[j],).text=datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(data) - 2).strftime("%Y-%m-%d")
                else:
                    ET.SubElement(root4,fields[j],).text=str(data)
            else:
                if j<2:
                    return False
                if j==2:                    
                    ET.SubElement(root4,fields[j],).text=str(df2.cell_value(rowx=i,colx=j))
                    ET.SubElement(root4,fields[j+1],).text=datetime.now().strftime("%Y-%m-%d")
                    ET.SubElement(root4,fields[j+2],).text=datetime.now().strftime("%Y-%m-%d")
                    df2._cell_types[i][3]=''
                    df2._cell_types[i][4]=''
        
    tree = ET.ElementTree(root)
    tree.write(outputFile)
    return True

c=getPriceUpdateXML('source.xlsx','price.xml')