import numpy as np
import matplotlib.pyplot as plt
scores = [85, 78, 92, 89, 67, 76, 94, 82, 91, 88, 75, 81, 96, 90, 79, 83, 77, 85, 98, 72]

mean_score = np.mean(scores)
median_score = np.median(scores)
q1 = np.percentile(scores, 25)
q3 = np.percentile(scores, 75)
iqr = q3 - q1
print("Mean Score:", mean_score)
print("Median Score:", median_score)
print("Q1 (25th percentile):", q1)
print("Q3 (75th percentile):", q3)
print("IQR (Interquartile Range):",iqr)
plt.boxplot(scores)
plt.title('Box Plot of Survey Scores')
plt.ylabel('Scores')
plt.show()
