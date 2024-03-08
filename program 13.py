import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    'student_id': [1, 2, 3, 4, 5],
    'test1_marks': [85, 70, 90, 65, 75],
    'test2_marks': [90, 75, 88, 70, 80]
}
df = pd.DataFrame(data)
summary = df.describe()
print(summary)
cov = df.cov()
print("\nCovariance Matrix:")
print(cov)
corr = df.corr()
print("\nCorrelation Matrix:")
print(corr)
m1 = df['test1_marks'].mean()
m2 = df['test2_marks'].mean()
print("Mean Test 1 Marks:",m1)
print("Mean Test 2 Marks:",m2)
v1 = df['test1_marks'].var()
v2 = df['test2_marks'].var()
print("Variance Test 1 Marks: ",v1)
print("Variance Test 2 Marks: ",v2)
plt.boxplot([df['test1_marks'], df['test2_marks']], labels=['Test 1', 'Test 2'])
plt.title('Boxplot of Test Scores')
plt.show()
