import pandas as pd
import numpy as np

n = [[1,2,3,4],[5,6,7,8],[4,5,6,7],[1,2,6,8]]
arr = np.array(n)
df = pd.DataFrame(arr, columns=['A','B','C','D'],index=['2015','2016','2017','2018'])
print(arr, '\n', df)
