import pandas as pd
data = {
    'customer_id': [101, 102, None, 104, 105],
    'product_name': ['Product A', 'Product B','Product C',None, 'Product E'],
    'price': [10, 20, 40, 50, None]
}
df = pd.DataFrame(data)
df.dropna(subset=['customer_id'], inplace=True)
df['price'].fillna(df['price'].mean(), inplace=True)
df['product_name'].fillna(df['product_name'].mode()[0], inplace=True)
print("DataFrame after handling missing values:")
print(df)
