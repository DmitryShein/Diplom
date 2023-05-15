import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

from time import sleep

subscription_key = '543f5e3d26764f089c50805b44fb1bf0'

cmdCode = 'TOTAL' #Есть еще TOTAL, ALL и просто коды товаров
partnerCode1 = '12'
partnerCode2 = '20'

# Извлечение данных в фрейм данных pandas
# getFinalData - возвращает фрейм данных, содержащий окончательные данные о торговле (ограничено 250 000 записей).
df_aistrade1 = comtradeapicall.getFinalData(subscription_key, typeCode = 'C', period = '2020', reporterCode = '643', cmdCode = cmdCode, partnerCode = partnerCode1, partner2Code = '0', freqCode='A', clCode = 'HS', flowCode='X', customsCode = 'C00', motCode = '0')

sleep(10.5)

df_aistrade2 = comtradeapicall.getFinalData(subscription_key, typeCode = 'C', period = '2020', reporterCode = '643', cmdCode = cmdCode, partnerCode = partnerCode2, partner2Code = '0', freqCode='A', clCode = 'HS', flowCode='X', customsCode = 'C00', motCode = '0')
#df_aistrade.head(5)
#На выходе репортер - партнер - товар - период - значение

added = pd.concat([df_aistrade1, df_aistrade2], axis=0)
print(added)

#Сейвим в эксель
#added.to_excel(r'C:\Users\Дмитрий\Documents\GitHub\Diplom\results\data.xlsx')