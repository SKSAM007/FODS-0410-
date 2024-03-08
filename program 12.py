import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [10000, 12000, 11000, 13000, 14000, 15000]
}
df = pd.DataFrame(data)
months = df['Month']
sales = df['Sales']
plt.plot(months, sales, marker='o', color='b', linestyle='-')
plt.title('Monthly Sales of Product X')
plt.show()
plt.scatter(months, sales, color='r')
plt.title('Monthly Sales of Product X')
plt.show()
plt.bar(months, sales, color='skyblue')
plt.title('Monthly Sales of Product X')
plt.show()
