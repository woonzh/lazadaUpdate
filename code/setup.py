# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 09:11:25 2017

@author: ASUS
"""

from cx_Freeze import setup, Executable
import sys

base = None
if sys.platform == "win32":
    base = "Console"

executables = [Executable("priceUpdate.py", base=base)]

import os
os.environ['TCL_LIBRARY'] = r'C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\ASUS\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

packages = ['idna','requests','json','os','urllib','hashlib','hmac','datetime','pytz','xml.etree.cElementTree','pandas','numpy','xlrd','sys']
options = {
    'build_exe': {

        'packages':packages,
        'include_files':['params.py','xmlGenerator.py','source.xlsx']
    },

}

setup(
    name = "lazada price updater",
    options = options,
    version = "1",
    description = 'Updates pricing / sales pricing & period to lazada based on seller SKU',
    executables = executables
)
