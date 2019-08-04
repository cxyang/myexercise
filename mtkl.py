import random
from var import VaR
import numpy as np
import scipy
import pandas as pd

# def M_C(num):
#     count = 0
#     for i in range(1, num+1):
#         x = random.uniform(0,1)
#         y = random.uniform(0,1)
#         if x**2 + y**2 < 1:
#             count += 1
#     return 4.0*count/num
# print(M_C(100000))
# print('--------------------------------------------------------------')
# x=np.array([[1 ,5 ,6] ,[4 ,3 ,9 ],[ 4 ,2 ,9],[ 4 ,7 ,2]])
# print(x)
# cov = np.cov(x)
# b_1 = scipy.linalg.cholesky(cov)
# b_2 = np.linalg.cholesky(cov)
# print(b_1)
print('**********')
# print(b_2)
# x = []
# for i in range(4):
#     xi = np.random.rand(10)
#     x.append(xi)
# x = np.array(x)
# print(x)
# print('----------------')
# R = np.dot(b_1, x)
# print(R)
# xi = np.random.normal(5,1.2,15)
# print(xi)
data = {
        'stock': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 4.6,4.7],
        'stock1':[1.4,1.7, 1.3, 1.8, 2.3, 2.1, 2.4,2.8],
        'stock2':[ 3.1, 3.5, 3.6, 3.7, 3.9, 4.2, 3.9, 4.0],
        'stock3':[ 4.1, 4.5, 4.6, 5.7, 3.9, 4.6, 3.8, 4.0],
        # 'stock4':[0,0,0,0,0,0,0,0]
        }
df = pd.DataFrame(data, index=[2000, 2001, 2002, 2001, 2002, 2003,2004,2005])
m = 2
f = 0.3

# Cov = np.cov(df.T)
#
# b = scipy.linalg.cholesky(Cov)
# print(b)
print('---------')
# def mtkl(r,w,a):
#     m = df.mean()
#     f = df.std()
#     Cov = np.cov(r)
#     b = scipy.linalg.cholesky(Cov)
#     print(b)
#     x = []
#     for i in range(len(r.T)):
#         xi = np.random.normal(m, f, 100)
#         x.append(xi)
#     x = np.array(x)
#     R = np.dot(b, x)
#     print(R)
#     y = np.dot(w.T, R)
#     y = sorted(y)
#     k = int(100 * a)
#     t = y[k-1] + (y[k]-y[k-1]) * (100*a-k)
#     print(t)
#     return t
cov = np.cov(df)
print(df.mean().mean())
print(df.var().std())

a = 0.97
w = np.array([0.2, 0.3, 0.3, 0.2])







