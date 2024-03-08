import numpy as np
from scipy import stats

amount = [20, 30, 40, 50, 40, 60, 30, 40, 50, 40, 30, 40, 50, 60]
mean = np.mean(amount)
mode = stats.mode(amount).mode
print("Mean purchase amount: ", mean)
print("Mode of the purchase amounts: ", mode)
