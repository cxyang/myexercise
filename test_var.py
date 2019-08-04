from var import VaR
import random
import pandas as pd
import math
import numpy as np
from scipy.stats import norm
from arch import arch_model
from functools import reduce

# 测试
data = {
        'stock': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 4.6,4.7],
        'stock1':[1.4,1.7, 1.3, 1.8, 2.3, 2.1, 2.4,2.8],
        'stock2':[ 3.1, 3.5, 3.6, 3.7, 3.9, 4.2, 3.9, 4.0],
        'stock3':[ 4.1, 4.5, 4.6, 5.7, 3.9, 3.2, 3.8, 4.0],
        'stock4':[1, 0, 0, 0, 0, 0, 0, 0],
        'stock5':[5, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0],
        'stock6':[1,1,1,1,1,2,1,1]
        }

df = pd.DataFrame(data, index=[2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007])
print(df)
print(df.std())
print('-------')
w = [0.1,0.2,0.1,0.13,0.17,0.1,0.1,0.1]
w = pd.DataFrame(w, index=df.index)
print(w)
print(w[5:100])
print('-------')
# for i in range(len(df.T)):
#     s = df.iloc[:,i]
#     res = pd.concat([s,w], axis=1)
#     res = res.sort_values(by=s.name , ascending=False)
#     # res = res[0:3]
#     for j in range(len(res)):
#         if sum(res[0][0:j])-0.7>=0:
#             # print(j)
#             # print(res[0][0:j])
#             # print(res.iloc[j-1,0])
#             r2 = res.iloc[j-1,0]
#             w2 = sum(res[0][0:j])
#             r1 = res.iloc[j-2,0]
#             w1 = sum(res[0][0:j-1])
#             # print(w2)
#             end = r1 + (r2-r1)*(0.7-w1)/(w2-w1)
#             print(end)
#             break
#         else:
#             continue
    # print(res)
# for k in range(len(res)):
#     res = sum(res[0][0:k])
#     print(res)
# df0 = df.fillna(0)
# df = df0.ix[:, (df0 != df0.iloc[0]).any()]
# # delete = list(set(df0.columns.values)^set(df.columns.values))
# delete = [item for item in df0.columns.values if item not in df.columns.values]
# print(delete)
# print('-----------------------------')
t = VaR()
a = 0.97
w = []
for i in range(len(df.T)):
         x = 1/len(df.T)
         w.append(x)
w = np.array(w)
# print(w)
# print(t.com_var(df,w,a))
# print(t.cvar(df,w,a))
# print(t.com_var(df, w, a, 2))
# print(t.mtkl(df, w, a))
print('----------------------------------')

# 权重
l = df.shape[1]
# weights = np.random.random(l)
# weights /= np.sum(weights)
# weights = np.array(weights)
print('****************************')
# # print(t.garch11(df,a))
# #print(t.var_week(df, a))
# print(t.com_var(df, w, a))

# print(t.com_var(df, w, a, 3))

# x = np.random.standard_normal(1000)
# print(x)

# k = int(len(df) * (a))
# t = l.iloc[k-1] + (l.iloc[k] - l.iloc[k-1])*(len(l)*a - k)
# print(t)
r = norm.ppf(0.03)
print(r)