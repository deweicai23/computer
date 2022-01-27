import pandas as pd
import numpy as np


print("test pull")
# date = pd.date_range('20170301', periods=8)
# df = pd.DataFrame(np.random.randn(8, 5), index=date, columns=['A', 'B', 'C', 'D', 'E'])
# print(df)
#
#
# df = pd.DataFrame({ "A":pd.Series(['17','87','57','39'], index=['a', 'b', 'c', 'd']), "B":pd.Timestamp('20210301'), "C":pd.Categorical(['1','2','3','4'])})
# print(df)

#df = pd.Series(['4','7','-5','3'], index=['Mon', 'Tue', 'Wed', 'Thu'])
#print(df)
# print("========================")
# df =pd.Series({"新北":400,"台中":280,"高雄":277})
# print(df)

# df = pd.DataFrame({ "City":pd.Series(['TaiZhong','TaiZhong']), "Year":(['2016','2017']), "Population":(['276', '278'])})
# print(df)

data = {'城市':['台中', '台中', '台中', '高雄', '高雄', '高雄',np.nan],
        '年份':[2016, 2017, 2018, 2016, 2017, 2018,2022],
        '人口數':[276, 278, 280, 277, 277, 277,np.nan]}
df = pd.DataFrame(data)
# df['中部'] = (df['城市']=='台中')
# df['負債'] = df['人口數'] * 100


# df['负债']=10000
# df['利率']=0.05
# df['年份']=2022
#
print(df)

# a = {"年份": ['2016', '2017', '2018'], "城市": ['台中', '台中', '台中'], "人口數": ['276', '278', '280'],"負債": [np.NaN, '1100.0', np.nan], "中部": ['True', 'True', 'True']}
# df3 = pd.DataFrame(a, index=['一', '二', '三'])
# print(df3)
#
# df5 = df.iloc[3]
# print(df5)

# print(df3.loc['二'])
print(df["年份"].iloc[3])
