import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
data = {
    'age': [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61],
    'body_fat_percentage': [9.5, 26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]
}

df = pd.DataFrame(data)
mean1 = df['age'].mean()
median1 = df['age'].median()
std1 = df['age'].std()

mean2 = df['body_fat_percentage'].mean()
median2 = df['body_fat_percentage'].median()
std2 = df['body_fat_percentage'].std()

print("Age Statistics:")
print("Mean:", mean1)
print("Median:",median1)
print("Standard Deviation:",std1)

print("\nBody Fat Percentage Statistics:")
print("Mean:", mean2)
print("Median:", median2)
print("Standard Deviation:", std2)

plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.boxplot(df['age'])
plt.title('Boxplot of Age')
plt.ylabel('Age')

plt.subplot(1, 2, 2)
plt.boxplot(df['body_fat_percentage'])
plt.title('Boxplot of Body Fat Percentage')
plt.ylabel('Body Fat Percentage')

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(df['age'], df['body_fat_percentage'])
plt.title('Scatter Plot of Age vs. Body Fat Percentage')
plt.xlabel('Age')
plt.ylabel('Body Fat Percentage')

plt.subplot(1, 2, 2)
stats.probplot(df['body_fat_percentage'], dist="norm", plot=plt)
plt.title('Q-Q Plot of Body Fat Percentage')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Ordered Values')

plt.tight_layout()
plt.show()
