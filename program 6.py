import numpy as np
itemprices = np.array([2.5, 3.0, 1.75, 4.25])  
quantities = np.array([3, 2, 1, 4])             
discount = 10                              
tax = 8
totalcosts = itemprices * quantities
subtotal = np.sum(totalcosts)
disamt = (discount / 100) * subtotal
tbt = subtotal - disamt
taxamt = (tax / 100) * tbt
total = tbt + taxamt
print("Total cost including discounts and taxes:", total)

