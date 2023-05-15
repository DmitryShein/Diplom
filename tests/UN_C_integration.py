#Импорт библиотек для работы с таблицами, графиками и массивами
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Импорт библиотеки UN Comtrade для получения данных
import comtradeapicall

#Импорт библиотеки для получения, и последующегос скрытия ключа
from getpass import getpass

#subscription_key = getpass('Введите ваш ключ: ')
subscription_key = '543f5e3d26764f089c50805b44fb1bf0'

def unc_request():
    