import pandas as pd
import numpy as np



#Series
s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])

#DataFrame
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': s,
     '自定义':'自定义'}

df=pd.DataFrame(d)
print(df)
#选取：
# 按行的索引，行号，索引值
# print("========================")
print(df.iloc[1])
# print(df.loc['e'])
# # 按列的名称，
# print("========================")
# print(df["two"]) # 单列
# print(df[["two","one"]])
# # 行列同时进行筛选，
# print("========================")
# print(df["two"].loc['b'])
# 模糊查询，大于0的所有数据
# print("========================")
# print(df[df['one']>0])
# # #多列
# # # 精准查询、
# print("========================")
# print(df[df['one']==3])