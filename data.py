import pandas as pd

file_path = r'C:\Users\User\PycharmProjects\House_Prices\dataset\train.csv'

df_train = pd.read_csv(file_path)

print(df_train.head())
