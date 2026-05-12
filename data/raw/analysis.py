import pandas as pd


pd.set_option('display.max_columns', None)


shopping_data = pd.read_csv("shopping.csv")

print(shopping_data.head())
print(shopping_data.info())
print(shopping_data.describe())