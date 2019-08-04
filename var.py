import random
import pandas as pd
import math
import scipy
import numpy as np
from scipy.stats import norm
from arch import arch_model


class VaR(object):

    def data(self, df):
        df0 = df.fillna(0)
        df = df0.ix[:, (df0 != df0.iloc[0]).any()]

        delete = [item for item in df0.columns.values if item not in df.columns.values]
        print('删除的股票：')
        print(delete)
        return df


# 历史模拟法
    # v:资产价值
    # a：置信水平，取值 99.5%， 99%， 95%
    # n：时间宽度，取值5年   (这里暂且把 n 理解为前n个数据)
    # r：周（5日）、月（21日）持有期收益率
    def var_hist(self, r, a):
        res = []
        for i in range(len(r.T)):
            s = r.iloc[:,i]
            s = s.sort_values()
            k = int(len(s) * a)
            t = s.iloc[k-1] + (s.iloc[k] - s.iloc[k-1])*(len(s)*a - k)
            res.append(t)
        return pd.Series(res)

#   蒙特卡洛模拟（Monte Carlo）
    def mtkl(self, r, w, a):
        # m = r.mean().mean()            #  1
        # f = r.std().var()              #  1
        Cov = np.cov(r.T)  # 2
        b = scipy.linalg.cholesky(Cov, lower=True)  # @2（矩阵Cov是否为正定，等否进行分解下三角）
        # print(b)                                          #  2
        x = []  # 3
        for i in range(len(r.T)):
            xi = np.random.standard_normal(1000)
            x.append(xi)
        x = np.array(x)
        R = np.dot(b, x)

        y = sorted(np.dot(w, R), reverse=True)  # 4
        k = int(1000 * a)  # 5
        res = y[k - 1] + (y[k] - y[k - 1]) * (1000 * a - k)  # 5
        return res
    # def var_m(self, r, a):
    #     res = []
    #     for i in range(len(r.T)):
    #         s = r.iloc[:, i]
    #         l = s.sort_values(ascending = False)
    #         k = int(len(l) * (1-a))
    #         res.append(l.iloc[k])
    #     return pd.Series(res)
    #
    # def var_d(self, r, a):
    #     res = self.var_week(r, a)
    #     res = map(lambda x: x / math.sqrt(5), res)
    #     return pd.Series(res)

    # 参数法
    # 使用pandas.ewma 计算 sigma ;
    # 使用arch包      计算 sigma ;
    # N^-1(1-a) :scipy.stats.norm.ppf(1-a)

    def ewma(self, R, a):
        z = norm.ppf(1 - a)
        R = np.array(R)
        return np.sqrt(0.94 * R.var(axis=0) + 0.06 * R[-1] ** 2) * (-z)

    def garch11(self, R, a):
        z = norm.ppf(1 - a)
        res = []
        for i in range(len(R.T)):
            garch11 = arch_model(R.iloc[:, i], p=1, q=1).fit(disp='off')
            # print(not garch11)
            res.append(np.sqrt(garch11.forecast().variance.iloc[-1, 0]))
        return pd.Series(res) *(-z)

    # 组合VaR
    def com_var(self, r, w, a, type=1):
        if type == 1:
            value_at_risk = self.ewma(r, a)
        elif type == 2:
            value_at_risk = self.var_hist(r, a)
        else:
            value_at_risk = self.garch11(r, a)

        corr = r.corr()
        p = (np.multiply(w, value_at_risk))
        # print('>>>',np.dot(corr, p), '<<<')
        res = np.sqrt(np.dot(p.T, np.dot(corr, p)))
        return res

        # for i in range(1000):                                     @3 按行循环还是按列循环？
                #     xi = np.random.standard_normal(len(r.T))
                #     x.append(xi)
                # # print(x)
                # x = np.array(x)                      #  3
                # R = np.dot(b, x.T)
        #------------------------------------------------
        # if r = r1:      #  使用r周                               @4 根据用户选择输入的数据，替换最大最小值
        #     R = np.clip(R, 1.5, 5.0)
        # elif r = r2:      #  使用r月
        #     R = np.clip(R, -0.9, 6.4）
        # print(R)

#   蒙特卡洛模拟
    def mtkl(self, r, w, a):
        # m = r.mean().mean()            #  1
        # f = r.std().var()              #  1
        Cov = np.cov(r.T)             #  2
        b = scipy.linalg.cholesky(Cov, lower=True)            #    @2（矩阵Cov是否为正定，等否进行分解下三角）
        # print(b)                                          #  2
        x = []                               #  3
        for i in range(len(r.T)):
            xi = np.random.standard_normal(1000)
            x.append(xi)
        x = np.array(x)
        R = np.dot(b, x)

        y = sorted(np.dot(w, R), reverse=True)   #  4
        k = int(1000 * a)                   #  5
        res = y[k - 1] + (y[k] - y[k - 1]) * (1000 * a - k)    #  5
        return res

#   蒙特卡洛模拟 输入日数据
    def mtkl_d(self, r, w, a, type=1):
        # m = r.mean().mean()            #  1
        # f = r.std().var()              #  1
        if type == 1:
            Cov = np.cov(r.T)  # 2
        elif type == 2:
            Cov = np.cov(r.T)
        else:
            Cov = np.cov(r.T)
        b = scipy.linalg.cholesky(Cov, lower=True)  # @2（矩阵Cov是否为正定，等否进行分解下三角）
        # print(b)                                          #  2
        x = []  # 3
        for i in range(len(r.T)):
            xi = np.random.standard_normal(1000)
            x.append(xi)
        x = np.array(x)
        R = np.dot(b, x)

        y = sorted(np.dot(w, R), reverse=True)  # 4
        k = int(1000 * a)  # 5
        res = y[k - 1] + (y[k] - y[k - 1]) * (1000 * a - k)  # 5
        return res

#   蒙特卡洛模拟 输入周数据
    def mtkl_w(self, r, w, a, type=1):
        # m = r.mean().mean()            #  1
        # f = r.std().var()              #  1
        if type == 1:
            Cov = np.cov(r.T)  # 2
        elif type == 2:
            Cov = np.cov(r.T)
        else:
            Cov = np.cov(r.T)
        b = scipy.linalg.cholesky(Cov, lower=True)  # @2（矩阵Cov是否为正定，等否进行分解下三角）
                                       #  2
        x = []  # 3
        for i in range(len(r.T)):
            xi = np.random.standard_normal(1000)
            x.append(xi)
        x = np.array(x)
        R = np.dot(b, x)
        R = np.clip(R, -0.4, 0.6)                    # 设置最小值最大值

        y = sorted(np.dot(w, R), reverse=True)  # 4
        k = int(1000 * a)  # 5
        res = y[k - 1] + (y[k] - y[k - 1]) * (1000 * a - k)  # 5
        return res

#   蒙特卡洛模拟 输入月数据
    def mtkl_m(self, r, w, a, type=1):
        # m = r.mean().mean()            #  1
        # f = r.std().var()              #  1
        if type == 1:
            Cov = np.cov(r.T)  # 2
        elif type == 2:
            Cov = np.cov(r.T)
        else:
            Cov = np.cov(r.T)
        b = scipy.linalg.cholesky(Cov, lower=True)  # @2（矩阵Cov是否为正定，等否进行分解下三角）
                                       #  2
        x = []  # 3
        for i in range(len(r.T)):
            xi = np.random.standard_normal(1000)
            x.append(xi)
        x = np.array(x)
        R = np.dot(b, x)
        R = np.clip(R, -0.9, 6.4)                    # 设置最小值最大值

        y = sorted(np.dot(w, R), reverse=True)  # 4
        k = int(1000 * a)  # 5
        res = y[k - 1] + (y[k] - y[k - 1]) * (1000 * a - k)  # 5
        return res

# 计算每支股票的cvar
    def cvar(self, r, w, a):
        cVaR = []
        var0 = self.com_var(r,w,a)
        col = r.columns.values
        for i in range(len(col)):
            # print(r.iloc[:,i])
            # print(col[i])
            r1 = r.drop([col[i]], axis=1, inplace=False)
            w1 = np.delete(w, [i])
            var1 = self.com_var(r1, w1, a)
            res = var0 - var1
            # print(res)
            cVaR.append(res)
        return cVaR



    # def comp(self, x):


