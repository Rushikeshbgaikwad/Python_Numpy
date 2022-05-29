import numpy as np
x = np.random.randint(0,500,25).reshape(5,5)
print("Original Array:")
print(x,"\n")
# xmin, xmax = x.min(), x.max()
# print("Minimum and Maximum Values:")
# print(xmin, xmax)

def max(x):
    r=x
    print("The maximum value in matrix is = ",r.max())

def min(x):
    r=x
    print("The minimum value in matrix is = ",r.min())

max(x)
min(x)
