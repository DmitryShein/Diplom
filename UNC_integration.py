import sys

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import comtradeapicall

#Обычный запрос на данные UN C
def get_request(request):

    print('Get request..')
    print('Ключ:', request['subscription_key'])
    print('Код товара:', request['cmdCode'])
    print('Страна:', request['reporterTxt'])
    print('Код страны:', request['reporterCode'])
    print('Партнер:', request['partтerTxt'])
    print('Код партнера:', request['partnerCode'])
    print('Период:', request['period'])
    print('Тип потока:', request['typeCode'])
    print('Тип периода:', request['freqCode'])
    print('Тип товара:', request['flowCode'])
    
    df_aistradeq = comtradeapicall.getFinalData(subscription_key = request['subscription_key'], typeCode = request['typeCode'], freqCode = request['freqCode'], clCode = 'HS', period = request['period'], reporterCode = request['reporterCode'], cmdCode = request['cmdCode'], flowCode=request['flowCode'], partnerCode = request['partnerCode'], partner2Code = None, customsCode = None, motCode = None)
    return df_aistradeq

#Сделать названия полей на русском
def transformation_to_russian(data):

    df = data.rename(columns={'typeCode': 'Тип (C/S)'})
    df = df.rename(columns={'freqCode': 'Тип периода'})
    df = df.drop('refPeriodId', axis = 1) 
    df = df.rename(columns={'refYear': 'Год'})
    df = df.rename(columns={'refMonth': 'Месяц (код)'})
    df = df.rename(columns={'period': 'Период'})
    df = df.rename(columns={'reporterCode': 'Код репортера'})
    df = df.drop('reporterISO', axis = 1) 
    df = df.drop('reporterDesc', axis = 1)
    df = df.drop('flowDesc', axis = 1)
    df = df.drop('partnerDesc', axis = 1) 
    df = df.rename(columns={'flowCode': 'Торговый поток'})
    df = df.rename(columns={'partnerCode': 'ISO партнера'})
    df = df.drop('partnerISO', axis = 1) 

    df = df.rename(columns={'partner2Code': 'Код 2го партнера '})
    df = df.drop('partner2ISO', axis = 1)
    df = df.drop('partner2Desc', axis = 1) 

    df = df.rename(columns={'classificationCode': 'Тип номенклатуры'})
    df = df.rename(columns={'classificationSearchCode': 'Код номенклатуры'})
    df = df.rename(columns={'isOriginalClassification': 'Стандарт классификации'})
    df = df.rename(columns={'cmdCode': 'Код товара'})
    df = df.drop('cmdDesc', axis = 1)
    df = df.drop('aggrLevel', axis = 1)
    df = df.rename(columns={'isLeaf': 'Эко'})
    
    df = df.drop('customsDesc', axis = 1)
    df = df.drop('mosCode', axis = 1)
    df = df.drop('motDesc', axis = 1)
    df = df.rename(columns={'motCode': 'Вид транспорта'})

    df = df.rename(columns={'qtyUnitCode': 'Код вида еденицы'})
    df = df.drop('qtyUnitAbbr', axis = 1)
    
    df = df.rename(columns={'qty': 'Стоимость еденицы'})

    df = df.rename(columns={'isQtyEstimated': 'Оценивается количество'})
    df = df.rename(columns={'altQtyUnitCode': 'Альт. кол-во ед.'})
    
    df = df.drop('altQtyUnitAbbr', axis = 1)

    df = df.rename(columns={'altQty': 'Альт. стоимость еденицы'})

    df = df.drop('isAltQtyEstimated', axis = 1)

    df = df.rename(columns={'netWgt': 'Вес нетто'})
    df = df.rename(columns={'isNetWgtEstimated': 'Оценивается нетто-весом'})

    df = df.drop('isGrossWgtEstimated', axis = 1)
    df = df.drop('grossWgt', axis = 1)

    df = df.rename(columns={'cifvalue': 'Стоимость по СФ, $'})
    df = df.drop('fobvalue', axis = 1)
    df = df.rename(columns={'primaryValue': 'Номинальная стоимость, $'})
    df = df.drop('legacyEstimationFlag', axis = 1)
    df = df.rename(columns={'isReported': 'Оповещения'})
    df = df.rename(columns={'isAggregate': 'Агрегация'})
    

    return df


#df_aistrade.to_excel(r'C:\Users\Дмитрий\Documents\GitHub\Diplom\results\data.xlsx')

