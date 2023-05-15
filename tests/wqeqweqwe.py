import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

subscription_key = '543f5e3d26764f089c50805b44fb1bf0'

cmdCode = '11' #Есть еще TOTAL, ALL и просто коды товаров
partnerCode = '112'

#period = '202001,202002'
# Извлечение данных в фрейм данных pandas
# getFinalData - возвращает фрейм данных, содержащий окончательные данные о торговле (ограничено 250 000 записей).
df_aistrade = comtradeapicall.getFinalData(subscription_key, typeCode = 'C', freqCode='A', clCode = 'HS', period = '2021', reporterCode = '156', cmdCode = 'TOTAL', flowCode='M', partnerCode = '0', partner2Code = None, customsCode = None, motCode = None)

#df_aistrade.head(5)
#На выходе репортер - партнер - товар - период - значение

print(df_aistrade)

#Сейвим в эксель
df_aistrade.to_excel(r'C:\Users\Дмитрий\Documents\GitHub\Diplom\results\data.xlsx')

