import pandas as pd
data = {
    'customer_id': [101, 102, 103, None, 105, 101],
    'product_name': ['Product A', 'Product B', None, 'Product D', 'Product E', 'Product A'],
    'price': [10, 20, None, 40, 50, 10]
}
df = pd.DataFrame(data)
miss = df.isnull().sum().sum()
print("Number of missing values: ",miss)
dup = df.duplicated().sum()
print("Number of duplicates: ",dup)
