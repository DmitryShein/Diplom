import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

subscription_key = '<YOUR KEY>' # comtrade api subscription key (from comtradedeveloper.un.org)
directory = '<OUTPUT DIR>'  # output directory for downloaded files

Commodity_code = '3006' #pharmaceutical goods
Commodity_code = '1006' #rice
Commodity_code = '7108' #non-monetary gold
Commodity_code = '9201' #piano
Commodity_code = '2709' #crude oil
Commodity_code = '0901' #coffee
Commodity_code = '6309' #secondhand/ worn clothing
Commodity_code = '1001' #wheat and meslin

# create an Empty DataFrame object
panDForig = pd.DataFrame()
# A list of periods (this is for monthly sets), this is to optimize the API calls and avoid timeout
period_start = '2019-01-01'
period_end = '2022-12-01'
periods = pd.date_range(period_start,period_end,
              freq='MS').strftime("%Y%m").tolist()

# convert periods list into string with comma delimiter
delim = ","
temp = list(map(str, periods))
period_string = delim.join(temp)
print(period_string)

# get all tariffline data for a specific commodity_code
# this is a long operation and it is better to use comtradeapicall._getTarifflineData instead of comtradeapicall.getTarifflineData
# the function will split the query into multiple API calls reducing risk of timeout and increasing response time
panDForig = comtradeapicall._getTarifflineData(subscription_key, typeCode='C', freqCode='M', clCode='HS',
                                             period=period_string,
                                             reporterCode=None, cmdCode=Commodity_code, flowCode='M',
                                             partnerCode=None, partner2Code=None, customsCode=None, motCode=None, maxRecords=None,
                                             format_output='JSON',
                                             countOnly=None, includeDesc=True)

#check number of records
print('Final row count is:', len(panDForig))