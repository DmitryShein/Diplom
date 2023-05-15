import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

subscription_key = '543f5e3d26764f089c50805b44fb1bf0'

cmdCode = 'ALL' #Есть еще TOTAL, ALL и просто коды товаров
partnerCode = '156'

#period = '202001,202002'
# Извлечение данных в фрейм данных pandas
# getFinalData - возвращает фрейм данных, содержащий окончательные данные о торговле (ограничено 250 000 записей).
df_aistrade = comtradeapicall.getFinalData(subscription_key, typeCode = 'C', period = '2020', reporterCode = '643', cmdCode = cmdCode, partnerCode = partnerCode, partner2Code = '0', freqCode='A', clCode = 'HS', flowCode='', customsCode = 'C00', motCode = '0')

#df_aistrade.head(5)
#На выходе репортер - партнер - товар - период - значение

print(df_aistrade)

#Сейвим в эксель
df_aistrade.to_excel(r'C:\Users\Дмитрий\Documents\GitHub\Diplom\results\data.xlsx')

