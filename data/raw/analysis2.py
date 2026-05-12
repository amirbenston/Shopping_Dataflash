import pandas as pd

pd.set_option('display.max_columns', None)

shopping_data = pd.read_csv("shopping.csv")

# Most popular color by season
color_counts = shopping_data.groupby(['Season', 'Color']).size().reset_index(name='count')
color_counts = color_counts.sort_values(['Season', 'count'], ascending=[True, False])
top_colors = color_counts.groupby('Season').head(1)
print(top_colors)





# Most popular clothing item by season
item_counts = shopping_data.groupby(['Season', 'Item Purchased']).size().reset_index(name='count')
item_counts = item_counts.sort_values(['Season', 'count'], ascending=[True, False])
top_items = item_counts.groupby('Season').head(1)
print(top_items)







# Effect of promo codes on purchase amount
promo_effect = shopping_data.groupby('Promo Code Used')['Purchase Amount (USD)'].agg(['count', 'mean', 'median'])
print(promo_effect)