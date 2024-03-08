import pandas as pd
data = {
    'customer_id': [101, 102, 101, 103, 102, 103, 104, 101],
    'order_date': ['2023-05-15', '2023-06-20', '2023-05-20', '2023-08-05', '2023-07-10', '2023-07-25', '2023-06-30', '2023-09-12'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product C', 'Product A', 'Product B'],
    'order_quantity': [3, 2, 1, 4, 2, 3, 2, 1]
}
df = pd.DataFrame(data)
topc = df.groupby('customer_id').size()
aoq = df.groupby('product_name')['order_quantity'].mean()
eod = df['order_date'].min()
lod = df['order_date'].max()
print("Total number of orders made by each customer:\n",topc)
print("\nAverage order quantity for each product:\n",aoq)
print("\nEarliest order date:", eod)
print("Latest order date:", lod)
