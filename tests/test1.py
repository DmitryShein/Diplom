# Install a pip comtradeapicall package in the current Jupyter kernel
import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

#from getpass import getpass
#subscription_key = getpass('Enter the API subscription_key: ')
subscription_key = '<543f5e3d26764f089c50805b44fb1bf0>'

countryISO = 'FRA'
baseYear = '2021'
flow = 'X'
noOfPeriod = 15

df_availableperiods = comtradeapicall.getFinalDataAvailability(subscription_key=subscription_key,typeCode='C',freqCode='M',clCode='HS',reporterCode=comtradeapicall.convertCountryIso3ToCode(countryISO),period=None)
df_availableperiods["period"] = df_availableperiods["period"].values.astype(str)
targetPeriod_list = ','.join(df_availableperiods.sort_values(by='period', ascending=False)['period'].head(noOfPeriod).to_list())

#get the top 4 digits exported commodities
#classic breakdown mode will set the partner2Code to World, customsCode to Total, and motCode to Total.
df_CA_BaseYear_4Digit = comtradeapicall._getFinalData(subscription_key, typeCode='C', freqCode='A', clCode='HS',period=baseYear,reporterCode=comtradeapicall.convertCountryIso3ToCode(countryISO),cmdCode='AG4', flowCode=flow, partnerCode=0, partner2Code=None, customsCode=None,motCode=None,breakdownMode='classic', includeDesc=True)

df_CA_BaseYear_4Digit.sort_values(by='primaryValue', ascending=False)[['cmdCode','cmdDesc','primaryValue']].head(5)

listofcmd = ','.join(df_CA_BaseYear_4Digit.sort_values(by='primaryValue', ascending=False)['cmdCode'].head(5).to_list())

df_CM_top5 = comtradeapicall._getFinalData(subscription_key, typeCode='C', freqCode='M', clCode='HS', period=targetPeriod_list, reporterCode=comtradeapicall.convertCountryIso3ToCode(countryISO),cmdCode=listofcmd, flowCode=flow, partnerCode=0, partner2Code=None, customsCode=None,motCode=None,
breakdownMode='classic', includeDesc=True)

df_top5 = df_CM_top5.copy()
df_top5['cmdLabel'] = 'HS' + df_top5['cmdCode'] + ':' + df_top5['cmdDesc'].str[0:20] + '...'
df_top5.set_index(['period'],inplace=True)
df_top5.set_index('cmdLabel',append=True).unstack()['primaryValue'].plot()