import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Temperature': [10, 12, 15, 20, 25, 28, 30, 29, 26, 22, 18, 14],
    'Rainfall': [50, 40, 30, 20, 10, 5, 5, 10, 15, 20, 30, 40]
}
df = pd.DataFrame(data)
months = df['Month']
temperatures = df['Temperature']
rainfalls = df['Rainfall']
plt.plot(months, temperatures, marker='o', color='b', linestyle='-')
plt.title('Monthly Temperature Data')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.show()
plt.scatter(months, rainfalls, color='r')
plt.title('Monthly Rainfall Data')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.show()
