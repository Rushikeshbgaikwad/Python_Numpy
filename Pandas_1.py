# import pandas as pd
#
# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
#
# myvar = pd.DataFrame(mydataset)
#
# print(myvar)

import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(10))
