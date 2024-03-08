import pandas as pd
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'order_date': ["2023-05-15", "2023-06-20", "2023-07-10", "2023-08-05", "2023-09-12","2023-12-15","2023-07-25","2023-01-05","2023-06-17","2023-10-10"],
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
}
df = pd.DataFrame(data)
print(df)
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.month
print("\nDataFrame after transformation:")
print(df)
