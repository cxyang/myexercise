
# 通过 robjects 方法调用R 语言代码及R 的包，示例如下：
r_code =
'''
# create a function 'f'
f <- function(r)
{
   2 * pi * r
}
# create a function 'f2'
f2 <- function(r)
{
   5 * pi * r
}
'''

robjects.r(r_code)

r_f = robjrcts.r['f']
r_f2 = robjects.r['f']
rsum = robjects.r['f']

def on_date(context.data):
    v = robjects.FloatVector(data['topen'].iloc[-1].values)
    # call r function
    print(rsum(v)[0])
    print(r_f(3)[0])
    print(r_f2(3)[0])






