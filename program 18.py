import numpy as np
w = np.array(["sunny", "cloudy", "rainy", "windy", "snowy"])
f = np.array([150, 100, 80, 50, 20])
mci = np.argmax(f)
mcw = w[mci]
print("Frequency distribution of weather conditions:")
for weather, freq in zip(w, f):
    print(f"Weather: {weather}, Frequency: {freq}")
print(f"\nThe most common weather type is: {mcw}")
