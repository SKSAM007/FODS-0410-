import pandas as pd
data1 = {
    'order_id': [1, 2, 3, 4, 5],
    'product_id': [101, 102, 103, 104, 105],
    'customer_id': [101, 102, 103, 104, 105]
}
data2 = {
    'product_id': [101, 102, 103, 104, 105],
    'product_name': ['Mobile', 'Laptop', 'Monitor', 'Refrigerator', 'TV'],
    'price': [10, 20, 30, 40, 50]
}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.merge(df1, df2, on='product_id')
print("Merged DataFrame:")
print(df3)
