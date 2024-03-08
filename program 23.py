import numpy as np
from scipy import stats

product1 = [50, 55, 52, 48, 53, 49, 51, 47, 50, 54]
product2 = [55, 58, 53, 50, 57, 52, 56, 54, 59, 51]

mean_product1 = np.mean(product1)
mean_product2 = np.mean(product2)

print("mean of product1",mean_product1)
print("mean of product1",mean_product2)


ci_product1 = stats.t.interval(0.9, len(product1) - 1, loc=mean_product1 )
ci_product2 = stats.t.interval(0.9, len(product2) - 1, loc=mean_product2 )

print("90% CI_prodect1",ci_product1)
print("90% CI_prodduct2",ci_product2)

t_stat, p_value = stats.ttest_ind(product1, product2)

alpha = 0.05
print("\nHypothesis Test:")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

if p_value < alpha:
    print("Reject the null hypothesis. There is a statistically significant difference in lifespans.")
else:
    print("Fail to reject the null hypothesis. There is no statistically significant difference in lifespans.")
