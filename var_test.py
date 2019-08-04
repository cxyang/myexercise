import random
import pandas as pd
import math
import numpy as np
from scipy.stats import norm
from arch import arch_model

def ewma(R):
    R = np.array(R)
    return np.sqrt(0.94*R.var(axis=0) + 0.06*R[-1]**2)


def garch11(R):
    res = []
    for i in range(len(R.T)):
        garch11 = arch_model(R.iloc[:,i],p=1,q=1).fit(disp='off')
        res.append(np.sqrt(garch11.forecast().variance.iloc[-1,0]))
    return pd.Series(res)


# 组合VaR
def com_var(r, w):
    s1 = r['stock']
    s2 = r['stock1']
    corr = r.corr()
    print(corr)
    res = np.dot(w.T, np.dot(corr, w))
    return res


# 测试
data = {
        #'year':[2000, 2001, 2002, 2001, 2002, 2003,2004,2005],
        'stock': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 4.6, 4.7],
        'stock1':[1.4, 1.7, 1.3, 1.8, 2.3, 2.1, 2.4, 2.8]
        }
df = pd.DataFrame(data, index=[2000, 2001, 2002, 2001, 2002, 2003,2004,2005])

# print(df)
# r = [20, 18, 15, 13, 12, 10, 16, 18,21]
a = 0.6
z = norm.ppf(1-a)
w = np.array([0.4, 0.6])
t_ewma = ewma(df) * (-z)
t_garch11 = garch11(df) * (-z)
comvar = com_var(df, w)

print(t_ewma)
print('****************************')
print(t_garch11)
print('****************************')
print(comvar)
