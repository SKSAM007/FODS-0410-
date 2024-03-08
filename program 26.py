import pandas as pd
import numpy as np
from scipy.stats import t
df = pd.read_csv("customer_reviews.csv")
ratings = df['reviewsrating']
sample_mean = np.mean(ratings)
sample_std = np.std(ratings, ddof=1) 
n = len(ratings)
confidence_level = 0.95
t_critical = t.ppf((1 + confidence_level) / 2, df=n-1)
margin_of_error = t_critical * (sample_std / np.sqrt(n))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print("Sample Mean Rating:", sample_mean)
print("Sample Standard Deviation:", sample_std)
print("Sample Size:", n)
print("Confidence Level:", confidence_level)
print("Margin of Error:", margin_of_error)
print("Confidence Interval:", confidence_interval)
