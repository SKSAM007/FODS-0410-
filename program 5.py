import numpy as np
fuel_efficiency = np.array([25, 30, 20, 35, 28, 22, 32, 26, 29, 31])
avg = np.mean(fuel_efficiency)
car1 = 30
car2 = 25
pi = ((car1 - car2) / car2) * 100
print("Average fuel efficiency across all car models:", avg)
print("Fuel efficiency of car model 1:", car1)
print("Fuel efficiency of car model 2:", car2)
print("Percentage improvement in fuel efficiency between car model 1 and car model 2:", pi, "%")
