import numpy as np
arr = [1,2,3,4,5,6,7,8,9]
l= len(arr)
window_size = 3
avr = []
for i in range (l):
    window_average = round(np.sum(arr[i:i + window_size]) / window_size,2)
    avr.append(window_average)
print(avr)
print(np.sum(arr[:]))
