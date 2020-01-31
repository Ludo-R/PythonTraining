#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:43:33 2020

@author: ludodata
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 14:06:50 2020

@author: ludodata
"""

from sqlalchemy import create_engine
import pandas as pd
import pymysql
import time



engine = create_engine("mysql+pymysql://root:sqlpwd@localhost/opendata")

def importcsv(link, table):
    print("Lecture des données")
    start_time = time.time()
    df = pd.read_excel(link)
    print("Données lu")
    df.to_sql(table, con = engine, if_exists='append', index = False)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))
        

importcsv('/Users/ludodata/naf2008_5_niveaux.xls', 'naf_2008_5n') 
