import pandas as pd
data={
    'customer_id':[1,2,3,4,5,6,7,8,9,10],
    'product_id':[101,102,103,104,105,106,107,108,109,110],
    'rating':[4,2,3,6,4,'2','5',3,9,4]
}
df=pd.DataFrame(data)
print(df)
def clean_column(df):
    df.dropna(subset=['rating'],inplace=True)
    df['rating']=pd.to_numeric(df['rating'])
    df=df[(df['rating']>=1)&(df['rating']<=5)]
    return df

df_1=clean_column(df)
print("\nData Frame after cleaning:")
print(df_1)
              
    
