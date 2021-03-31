# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:08:36 2020

@author: Eeshan
"""

# Objective here is to find call and put purchases on Nifty 50, following a risk reduction approach of hedging on expiration.
# Other, more important objective is to constantly monitor the market for selling options.
# Final option is to explore the relations between different stocks, indices, futures, calls and puts.
import pandas as pd
import numpy as np
#from pandas import read_html

#url = "http://www.nseindia.com/option-chain"
#dflist = dflist = pd.io.html.read_html(url)
df = pd.read_csv(r'option-chain-equity-derivatives-apr-30-20-04-20t1120.csv',header = 1) #option-chain-equity-derivatives-apr-30-15-04-20t1445
#option-chain-equity-derivatives-apr-30-15-04-20t1530.csv
underlying = 9,282.75#9225.20#8925.30 #8956.95
#df = df.drop(['Unnamed:0'],axis = 1) This does not work for some silly reason
#df = df.drop(df.iloc[:,0],axis = 1)
df = df.drop(df.columns[[0]],axis = 1)
df = df.drop(df.columns[[-1]],axis = 1)

'''' Convert all data to float here'''
for i in range(len(df.columns)):
    for j in range(len(df.index)):
        if(df.iloc[j,i] == '-'):
            df.iloc[j,i] = 0
        elif(len(df.iloc[j,i]) > 3):
            df.iloc[j,i] = df.iloc[j,i].replace(',','')
            df.iloc[j,i] = float(df.iloc[j,i])
        else:
            df.iloc[j,i] = float(df.iloc[j,i])

#for i in range(len(df.index)):
c_frame = df.iloc[:,0:11][(df['OI'] > 0) & (underlying - df['STRIKE PRICE'] > df['ASK PRICE'])]
c_frame['Profit'] = underlying - c_frame['STRIKE PRICE']- c_frame['ASK PRICE']
c_frame = c_frame.sort_values('Profit',axis = 0, ascending = False)
#df['v_diff'] = underlying - df['STRIKE PRICE']
p_frame = df.iloc[:,10:21][(df['OI.1'] > 0) & (df['STRIKE PRICE'] - underlying > df['ASK PRICE.1'])]
p_frame['Profit'] = p_frame['STRIKE PRICE'] - underlying - p_frame['ASK PRICE.1']
p_frame = p_frame.sort_values('Profit',axis = 0,ascending = False)

c_frame.to_csv(r'Reports\apr-30-17-04-20t1015_calls.csv')
#df.to_csv(r'Reports\apr-30-15-04-20t1445_options.csv')




