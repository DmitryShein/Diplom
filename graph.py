import pandas as pd
import matplotlib.pyplot as plt

import numpy as np

def test_data_reporter():
    df = pd.read_excel('C:/Users/Дмитрий/Documents/GitHub/Diplom/results/reporter_all_patner/Mongolia X.xlsx')
    return df


#def test_data_trade():
#    df = pd.read_excel('C:/Users/Дмитрий/Documents/GitHub/Diplom/results/Full_reporter_trade_info/M_afg_to_china.xlsx')
#    return df

#создать график для товарного отчета
def trade_graphic(df, type):

    plt.clf()

    if type == 'Рейтинг крупнейших сделок (6 разрядов GS)':
        graphic = graphic_gs(df, 6)

    elif type == 'Рейтинг крупнейших сделок (4 разрядов GS)':
        graphic = graphic_gs(df, 4)

    elif type == 'Рейтинг крупнейших сделок (2 разрядов GS)':
        graphic = graphic_gs(df, 2)

    elif type == 'Крупнейшие торговые партнеры (год)':
        graphic = graphic_rep(df, 1)

    elif type == 'Крупнейшие торговые партнеры (5 лет)':
        graphic = graphic_rep(df, 5)

    elif type == 'Крупнейшие торговые партнеры (10 лет)':
        graphic = graphic_rep(df, 10)

    elif type == 'Динамика торговли в разрезе 10 лет':
        graphic = graphic_dinamic(df)

    else:
        print('Не найден подходящий тип графика')
        graphic = None
    
    return graphic

def graphic_dinamic(df):
    df = df[['Partner', 'Product code','Product label', "'Reporter exp to partn, $, 2012", "'Reporter exp to partn, $, 2013", "'Reporter exp to partn, $, 2014", "'Reporter exp to partn, $, 2015", "'Reporter exp to partn, $, 2016", "'Reporter exp to partn, $, 2017", "'Reporter exp to partn, $, 2018", "'Reporter exp to partn, $, 2019", "'Reporter exp to partn, $, 2020","'Reporter exp to partn, $, 2021"]]
    df = df.rename(columns={"'Reporter exp to partn, $, 2012":'2013'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2013":'2014'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2014":'2015'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2015":'2016'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2016":'2017'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2017":'2018'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2018":'2019'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2019":'2020'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2020":'2021'})
    df = df.rename(columns={"'Reporter exp to partn, $, 2021":'2022'})
    df = df[df['Product code'] == 'TOTAL']
    df = df.drop(df[df['Partner'] == 'World'].index)
    df = df.sort_values(by="2022", ascending=False).head(10)

    df = df[['Partner', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']]

    # создать линейный график

    df.set_index('Partner', inplace=True)
    df.transpose().plot(kind='line', figsize=(10,10))

    plt.xlabel('Год')
    plt.ylabel('Value, $')
    plt.title('Динамика торговли в разрезе 10 лет')


    fig = plt.gcf()

    return fig 

     
    
    
def graphic_rep(df, years):
    if years == 1:

        df = df[['Partner', 'Product code','Product label', "'Reporter exp to partn, $, 2021"]]

        df = df[df['Product code'] == 'TOTAL']
        df = df.drop(df[df['Partner'] == 'World'].index)

        df = df.sort_values(by="'Reporter exp to partn, $, 2021", ascending=False).head(10)

        plt.barh(df['Partner'], df["'Reporter exp to partn, $, 2021"])

        plt.title('Крупнейшие торговые партнеры за последний год')
        plt.xlabel('Сумма, $')
        plt.ylabel('Партнер')
        plt.gca().invert_yaxis()

        # вызываем функцию для автоматического подбора размеров и расположения элементов
        plt.tight_layout()

        fig = plt.gcf()

        return fig 

    elif years == 5:
        df['Sum 5 years'] = df[["'Reporter exp to partn, $, 2017", "'Reporter exp to partn, $, 2018", "'Reporter exp to partn, $, 2019", "'Reporter exp to partn, $, 2020","'Reporter exp to partn, $, 2021"]].sum(axis=1)
        df = df[['Partner', 'Product code','Product label', 'Sum 5 years']]
        
        df = df[df['Product code'] == 'TOTAL']
        df = df.drop(df[df['Partner'] == 'World'].index)

        df = df.sort_values(by="Sum 5 years", ascending=False).head(10)

        plt.barh(df['Partner'], df["Sum 5 years"])

        plt.title('Крупнейшие торговые партнеры за последние 5 лет')
        plt.xlabel('Сумма, $')
        plt.ylabel('Партнер')
        plt.gca().invert_yaxis()

        # вызываем функцию для автоматического подбора размеров и расположения элементов
        plt.tight_layout()

        fig = plt.gcf()
        return fig 

    elif years == 10:
        df['Sum 10 years'] = df[["'Reporter exp to partn, $, 2012", "'Reporter exp to partn, $, 2013", "'Reporter exp to partn, $, 2014", "'Reporter exp to partn, $, 2015", "'Reporter exp to partn, $, 2016", "'Reporter exp to partn, $, 2017", "'Reporter exp to partn, $, 2018", "'Reporter exp to partn, $, 2019", "'Reporter exp to partn, $, 2020","'Reporter exp to partn, $, 2021"]].sum(axis=1)
        df = df[['Partner', 'Product code','Product label', 'Sum 10 years']]
        
        df = df[df['Product code'] == 'TOTAL']
        df = df.drop(df[df['Partner'] == 'World'].index)

        df = df.sort_values(by="Sum 10 years", ascending=False).head(10)
        plt.barh(df['Partner'], df["Sum 10 years"])

        plt.title('Крупнейшие торговые партнеры за последние 10 лет')
        plt.xlabel('Сумма, $')
        plt.ylabel('Партнер')
        plt.gca().invert_yaxis()

        # вызываем функцию для автоматического подбора размеров и расположения элементов
        plt.tight_layout()

        fig = plt.gcf()

        return fig 
    else:
        pass

def graphic_gs(df, gs):
    df = df[df['Код товара'].apply(len) == gs]
    df = df.sort_values(by='Номинальная стоимость, $', ascending=False).head(10)

    df['Оповещения'] = df['Код товара'].map(product_codes.set_index('ProductCode')['Product Description'])
    df['Оповещения'] = df['Оповещения'].apply(cut_text)

    df['empty'] = ' - '
    df['new_col1'] = df['Оповещения'].astype(str) + df['empty'].astype(str)
    df['new_col']= df['new_col1'].astype(str) + df['Код товара'].astype(str)

    plt.barh(df['new_col'], df['Номинальная стоимость, $'])

    # создаем словарь соответствия значений
    mapping = {row['Код товара']: row['Оповещения'] for _, row in df.iterrows()}
    for el in mapping:
        mapping[el] = str(el) + ' - ' + mapping[el]

    # создаем легенду
    #legend = [plt.Line2D([0], [0], color='blue', lw=2, label=mapping[k]) for k in mapping]


    #plt.legend(handles=legend, fontsize=8)

    plt.title('Рейтинг крупнейших сделок')
    plt.xlabel('Код товара')
    plt.ylabel('Value, $')
    plt.gca().invert_yaxis()

    # вызываем функцию для автоматического подбора размеров и расположения элементов
    plt.tight_layout()

    fig = plt.gcf()
    return  fig 
    
def cut_text(text):
    text = str(text)
    return ' '.join(text.split()[:4])



#test_df1 = test_data_reporter()

#test_df2 = test_data_trade()



product_codes = pd.read_excel('C:/Users/Дмитрий/Documents/GitHub/Diplom/reference/Product_codes1.xlsx')

#Запускаем