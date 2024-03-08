import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'num_bedrooms': [3, 4, 2, 5, 3],
    'area_sqft': [1500, 1800, 1200, 2000, 1600],
    'listing_price': [250000, 350000, 200000, 450000, 300000]
}
df = pd.DataFrame(data)
avg_p = df.groupby('location')['listing_price'].mean()
num_4_b = (df['num_bedrooms'] > 4).sum()
larea = df['area_sqft'].max()
print("Average listing price of properties in each location:",avg_p)
print("\nNumber of properties with more than four bedrooms:", num_4_b)
print("\nProperty with the largest area:",larea)
