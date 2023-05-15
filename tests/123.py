import pandas
import os

current_dir = os.getcwd()

excel_data_df = pandas.read_excel(os.path.join(current_dir,'reference', 'Product_codes.xlsx'), sheet_name='HS Nomenclature')
print(excel_data_df)
excel_data_df.to_csv (os.path.join(current_dir,'reference', 'UN_goods_codes.csv'), index= False )