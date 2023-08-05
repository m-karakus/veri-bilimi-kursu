from pytrends.request import TrendReq

pytrends = TrendReq(hl="tr-TR", tz=-180, geo= "TR")
df = pytrends.trending_searches(pn='turkey') #daily search term
column_names = ['Topic']
df.columns = column_names
print(df)

