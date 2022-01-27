import pandas as pd
import numpy as np


s=pd.Series([i*2 for i in range(1,11)])
print(s)

#
# s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)
#
# dates = pd.date_range('20130101', periods=6)
# print(dates)
#
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)


#
df=pd.DataFrame({"A":1,"B":pd.Timestamp("20170301"),"C":pd.Categorical(["police","student","teacher","doctor"])})
print(df)


