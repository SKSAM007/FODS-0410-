import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind
control_group = [52, 48, 50, 55, 49, 47, 53, 51, 48, 50, 49, 54, 52, 56, 50, 48, 53, 47, 51, 49]
treatment_group = [62, 58, 63, 59, 60, 57, 61, 59, 64, 60, 58, 62, 63, 61, 60, 58, 59, 62, 64, 61]

t_statistic, p_value = ttest_ind(control_group, treatment_group)

print("P-value:", p_value)
plt.figure(figsize=(10, 6))

plt.hist(control_group, bins=20, alpha=0.5, label='Control Group (Placebo)')
plt.hist(treatment_group, bins=20, alpha=0.5, label='Treatment Group (New Drug)')

plt.axvline(np.mean(control_group), color='blue', linestyle='dashed', linewidth=1)
plt.axvline(np.mean(treatment_group), color='orange', linestyle='dashed', linewidth=1)

plt.legend()
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Control and Treatment Groups')

# Printing the p-value
plt.text(30, 10, f'p-value: {p_value:.4f}', fontsize=12, bbox=dict(facecolor='white', alpha=0.5))

plt.show()

