import pandas as pd


data = [[1, 'S8', 1000], [2, 'G4', 800], [3, 'iPhone', 1400]]
product = pd.DataFrame(data, columns=['product_id', 'product_name', 'unit_price']).astype({'product_id':'Int64', 'product_name':'object', 'unit_price':'Int64'})
data = [[1, 1, 1, '2019-01-21', 2, 2000], [1, 2, 2, '2019-02-17', 1, 800], [2, 2, 3, '2019-06-02', 1, 800], [3, 3, 4, '2019-05-13', 2, 2800]]
sales = pd.DataFrame(data, columns=['seller_id', 'product_id', 'buyer_id', 'sale_date', 'quantity', 'price']).astype({'seller_id':'Int64', 'product_id':'Int64', 'buyer_id':'Int64', 'sale_date':'datetime64[ns]', 'quantity':'Int64', 'price':'Int64'})

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(sales, product, on = 'product_id', how = 'left')
    grouped = merged.groupby(['product_id', 'product_name']).agg({'sale_date': ['min', 'max']}).reset_index()
    # Manually set the column names
    grouped.columns = ['product_id', 'product_name', 'min_sale', 'max_sale']
    grouped= grouped[(grouped['min_sale']>='2019-01-01') & (grouped['max_sale']<='2019-03-31')][['product_id','product_name']]
    return grouped

df_m = sales_analysis(sales, product)
print(df_m.head(10))

def sales_analysis1(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    values = sales[(sales['sale_date']>'2019-03-31') | (sales['sale_date']<'2019-01-01')]['product_id']
    print(type(values))
    print(values)

    filtered_df = sales[~sales['product_id'].isin(values)]['product_id']
    print('\n Filtered df')
    print(filtered_df)
    product = product[product['product_id'].isin(filtered_df)]
    print('\nProduct df')
    print(product)
    return product

df_n = sales_analysis1(sales, product)
