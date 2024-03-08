import numpy as np
data = np.genfromtxt('house_data.csv', delimiter=',')
b = 1
sale = 3
b4r = data[:, b] > 4
h4b = data[b4r]
avg = np.mean(h4b[:, sale])
print("Average sale price of houses with more than four bedrooms:", avg)
