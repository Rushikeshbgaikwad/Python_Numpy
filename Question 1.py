import numpy as np

arr = np.array([1, 2, 3, 4, 5])
column = 5

gfg = np.vander(arr, column, increasing=False)
gfg1 = np.vander(arr, column, increasing=True)

ru=np.column_stack([arr**(column-1-i) for i in range(column)])
ru1=np.column_stack([arr**(column-1-i) for i in range(column-1,0-1,-1)])
# for i in range(column):
#     ru = np.column_stack([arr ** (column - 1 - i)])
# for i in range(column-1,0-1,-1):
#     ru1 = np.column_stack([arr ** (column - 1 - i)])


print("This is matrix with increasing 'False'")
print(ru,"\n")
print("This is matrix with increasing 'True'")
print(ru1)


# print("This is matrix with increasing 'False'")
# print(gfg,"\n")
# print("This is matrix with increasing 'True'")
# print(gfg1)