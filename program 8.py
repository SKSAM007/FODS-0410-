import pandas as pd
data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G'],
    'quantity_sold': [5, 2, 4, 6, 8, 4, 3 ]
}
df = pd.DataFrame(data)
ps = df.groupby('product_name')['quantity_sold'].sum()
top_p = ps.sort_values(ascending=False)
top_5 = top_p.head()
print("Top 5 products sold the most in the past month:\n",top_5)
