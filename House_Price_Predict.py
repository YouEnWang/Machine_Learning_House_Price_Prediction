#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
import seaborn as sns
# 讓matplotlib顯示中文
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
#import dataset
df = pd.read_csv("num_all.csv")
df_num = pd.read_csv(r'num_all.csv', encoding = 'utf_8_sig')
df_dis = pd.read_csv(r'dis_all.csv', encoding = 'utf_8_sig')
df_only_house = pd.read_csv(r'real_price_only_house_chungli.csv', encoding = 'utf_8_sig')
df_nearest_avg_price = pd.read_csv(r'real_price_only_house_chungli_price.csv', encoding = 'utf_8_sig')
#observing dataset
df.head()
df.describe()
df_num_show = df.describe().T
df.info()
df_only_house.describe()
df_only_house['單價元平方公尺'].hist(bins=100)


# bins = [0, 5, 10, 15, 20]
# plt.hist(df_num['atm_200_300'],bins, histtype='bar', rwidth=1)
# plt.show()


# 將Atm做分組
# df_num['atm_0_100 Class','atm_100_200 Class','atm_200_300 Class','atm_300_400 Class','atm_400_500 Class','atm_500_600 Class','atm_600_700 Class','atm_700_800 Class','atm_800_900 Class','atm_900_1000 Class'] = np.nan
df_num.loc[ (df_num.atm_0_100>=0) & (df_num.atm_0_100<=5), 'atm_0_100 Class'] = 1
df_num.loc[ (df_num.atm_0_100>=6) & (df_num.atm_0_100<=10), 'atm_0_100 Class'] = 2
df_num.loc[ (df_num.atm_0_100>=11) & (df_num.atm_0_100<=20), 'atm_0_100 Class'] = 3

df_num.loc[ (df_num.atm_100_200>=0) & (df_num.atm_100_200<=5), 'atm_100_200 Class'] = 1
df_num.loc[ (df_num.atm_100_200>=6) & (df_num.atm_100_200<=10), 'atm_100_200 Class'] = 2
df_num.loc[ (df_num.atm_100_200>=11) & (df_num.atm_100_200<=20), 'atm_100_200 Class'] = 3

df_num.loc[ (df_num.atm_200_300>=0) & (df_num.atm_200_300<=5), 'atm_200_300 Class'] = 1
df_num.loc[ (df_num.atm_200_300>=6) & (df_num.atm_200_300<=10), 'atm_200_300 Class'] = 2
df_num.loc[ (df_num.atm_200_300>=11) & (df_num.atm_200_300<=20), 'atm_200_300 Class'] = 3

df_num.loc[ (df_num.atm_300_400>=0) & (df_num.atm_300_400<=5), 'atm_300_400 Class'] = 1
df_num.loc[ (df_num.atm_300_400>=6) & (df_num.atm_300_400<=10), 'atm_300_400 Class'] = 2
df_num.loc[ (df_num.atm_300_400>=11) & (df_num.atm_300_400<=20), 'atm_300_400 Class'] = 3

df_num.loc[ (df_num.atm_400_500>=0) & (df_num.atm_400_500<=5), 'atm_400_500 Class'] = 1
df_num.loc[ (df_num.atm_400_500>=6) & (df_num.atm_400_500<=10), 'atm_400_500 Class'] = 2
df_num.loc[ (df_num.atm_400_500>=11) & (df_num.atm_400_500<=20), 'atm_400_500 Class'] = 3

df_num.loc[ (df_num.atm_500_600>=0) & (df_num.atm_500_600<=5), 'atm_500_600 Class'] = 1
df_num.loc[ (df_num.atm_500_600>=6) & (df_num.atm_500_600<=10), 'atm_500_600 Class'] = 2
df_num.loc[ (df_num.atm_500_600>=11) & (df_num.atm_500_600<=20), 'atm_500_600 Class'] = 3

df_num.loc[ (df_num.atm_600_700>=0) & (df_num.atm_600_700<=5), 'atm_600_700 Class'] = 1
df_num.loc[ (df_num.atm_600_700>=6) & (df_num.atm_600_700<=10), 'atm_600_700 Class'] = 2
df_num.loc[ (df_num.atm_600_700>=11) & (df_num.atm_600_700<=20), 'atm_600_700 Class'] = 3

df_num.loc[ (df_num.atm_700_800>=0) & (df_num.atm_700_800<=5), 'atm_700_800 Class'] = 1
df_num.loc[ (df_num.atm_700_800>=6) & (df_num.atm_700_800<=10), 'atm_700_800 Class'] = 2
df_num.loc[ (df_num.atm_700_800>=11) & (df_num.atm_700_800<=20), 'atm_700_800 Class'] = 3

df_num.loc[ (df_num.atm_800_900>=0) & (df_num.atm_800_900<=5), 'atm_800_900 Class'] = 1
df_num.loc[ (df_num.atm_800_900>=6) & (df_num.atm_800_900<=10), 'atm_800_900 Class'] = 2
df_num.loc[ (df_num.atm_800_900>=11) & (df_num.atm_800_900<=20), 'atm_800_900 Class'] = 3

df_num.loc[ (df_num.atm_900_1000>=0) & (df_num.atm_900_1000<=5), 'atm_900_1000 Class'] = 1
df_num.loc[ (df_num.atm_900_1000>=6) & (df_num.atm_900_1000<=10), 'atm_900_1000 Class'] = 2
df_num.loc[ (df_num.atm_900_1000>=11) & (df_num.atm_900_1000<=20), 'atm_900_1000 Class'] = 3

# 將銀行做分組
df_num.loc[ (df_num.銀行_0_100>=0) & (df_num.銀行_0_100<=5), '銀行_0_100 Class'] = 1
df_num.loc[ (df_num.銀行_0_100>=6) & (df_num.銀行_0_100<=10), '銀行_0_100 Class'] = 2
df_num.loc[ (df_num.銀行_0_100>=11) & (df_num.銀行_0_100<=20), '銀行_0_100 Class'] = 3

df_num.loc[ (df_num.銀行_100_200>=0) & (df_num.銀行_100_200<=5), '銀行_100_200 Class'] = 1
df_num.loc[ (df_num.銀行_100_200>=6) & (df_num.銀行_100_200<=10), '銀行_100_200 Class'] = 2
df_num.loc[ (df_num.銀行_100_200>=11) & (df_num.銀行_100_200<=20), '銀行_100_200 Class'] = 3

df_num.loc[ (df_num.銀行_200_300>=0) & (df_num.銀行_200_300<=5), '銀行_200_300 Class'] = 1
df_num.loc[ (df_num.銀行_200_300>=6) & (df_num.銀行_200_300<=10), '銀行_200_300 Class'] = 2
df_num.loc[ (df_num.銀行_200_300>=11) & (df_num.銀行_200_300<=20), '銀行_200_300 Class'] = 3

df_num.loc[ (df_num.銀行_300_400>=0) & (df_num.銀行_300_400<=5), '銀行_300_400 Class'] = 1
df_num.loc[ (df_num.銀行_300_400>=6) & (df_num.銀行_300_400<=10), '銀行_300_400 Class'] = 2
df_num.loc[ (df_num.銀行_300_400>=11) & (df_num.銀行_300_400<=20), '銀行_300_400 Class'] = 3

df_num.loc[ (df_num.銀行_400_500>=0) & (df_num.銀行_400_500<=5), '銀行_400_500 Class'] = 1
df_num.loc[ (df_num.銀行_400_500>=6) & (df_num.銀行_400_500<=10), '銀行_400_500 Class'] = 2
df_num.loc[ (df_num.銀行_400_500>=11) & (df_num.銀行_400_500<=20), '銀行_400_500 Class'] = 3

df_num.loc[ (df_num.銀行_500_600>=0) & (df_num.銀行_500_600<=5), '銀行_500_600 Class'] = 1
df_num.loc[ (df_num.銀行_500_600>=6) & (df_num.銀行_500_600<=10), '銀行_500_600 Class'] = 2
df_num.loc[ (df_num.銀行_500_600>=11) & (df_num.銀行_500_600<=20), '銀行_500_600 Class'] = 3

df_num.loc[ (df_num.銀行_600_700>=0) & (df_num.銀行_600_700<=5), '銀行_600_700 Class'] = 1
df_num.loc[ (df_num.銀行_600_700>=6) & (df_num.銀行_600_700<=10), '銀行_600_700 Class'] = 2
df_num.loc[ (df_num.銀行_600_700>=11) & (df_num.銀行_600_700<=20), '銀行_600_700 Class'] = 3

df_num.loc[ (df_num.銀行_700_800>=0) & (df_num.銀行_700_800<=5), '銀行_700_800 Class'] = 1
df_num.loc[ (df_num.銀行_700_800>=6) & (df_num.銀行_700_800<=10), '銀行_700_800 Class'] = 2
df_num.loc[ (df_num.銀行_700_800>=11) & (df_num.銀行_700_800<=20), '銀行_700_800 Class'] = 3

df_num.loc[ (df_num.銀行_800_900>=0) & (df_num.銀行_800_900<=5), '銀行_800_900 Class'] = 1
df_num.loc[ (df_num.銀行_800_900>=6) & (df_num.銀行_800_900<=10), '銀行_800_900 Class'] = 2
df_num.loc[ (df_num.銀行_800_900>=11) & (df_num.銀行_800_900<=20), '銀行_800_900 Class'] = 3

df_num.loc[ (df_num.銀行_900_1000>=0) & (df_num.銀行_900_1000<=5), '銀行_900_1000 Class'] = 1
df_num.loc[ (df_num.銀行_900_1000>=6) & (df_num.銀行_900_1000<=10), '銀行_900_1000 Class'] = 2
df_num.loc[ (df_num.銀行_900_1000>=11) & (df_num.銀行_900_1000<=20), '銀行_900_1000 Class'] = 3

# 將咖啡廳做分組
df_num.loc[ (df_num.咖啡廳_0_100>=0) & (df_num.咖啡廳_0_100<=5), '咖啡廳_0_100 Class'] = 1
df_num.loc[ (df_num.咖啡廳_0_100>=6) & (df_num.咖啡廳_0_100<=10), '咖啡廳_0_100 Class'] = 2
df_num.loc[ (df_num.咖啡廳_0_100>=11) & (df_num.咖啡廳_0_100<=20), '咖啡廳_0_100 Class'] = 3

df_num.loc[ (df_num.咖啡廳_100_200>=0) & (df_num.咖啡廳_100_200<=5), '咖啡廳_100_200 Class'] = 1
df_num.loc[ (df_num.咖啡廳_100_200>=6) & (df_num.咖啡廳_100_200<=10), '咖啡廳_100_200 Class'] = 2
df_num.loc[ (df_num.咖啡廳_100_200>=11) & (df_num.咖啡廳_100_200<=20), '咖啡廳_100_200 Class'] = 3

df_num.loc[ (df_num.咖啡廳_200_300>=0) & (df_num.咖啡廳_200_300<=5), '咖啡廳_200_300 Class'] = 1
df_num.loc[ (df_num.咖啡廳_200_300>=6) & (df_num.咖啡廳_200_300<=10), '咖啡廳_200_300 Class'] = 2
df_num.loc[ (df_num.咖啡廳_200_300>=11) & (df_num.咖啡廳_200_300<=20), '咖啡廳_200_300 Class'] = 3

df_num.loc[ (df_num.咖啡廳_300_400>=0) & (df_num.咖啡廳_300_400<=5), '咖啡廳_300_400 Class'] = 1
df_num.loc[ (df_num.咖啡廳_300_400>=6) & (df_num.咖啡廳_300_400<=10), '咖啡廳_300_400 Class'] = 2
df_num.loc[ (df_num.咖啡廳_300_400>=11) & (df_num.咖啡廳_300_400<=20), '咖啡廳_300_400 Class'] = 3

df_num.loc[ (df_num.咖啡廳_400_500>=0) & (df_num.咖啡廳_400_500<=5), '咖啡廳_400_500 Class'] = 1
df_num.loc[ (df_num.咖啡廳_400_500>=6) & (df_num.咖啡廳_400_500<=10), '咖啡廳_400_500 Class'] = 2
df_num.loc[ (df_num.咖啡廳_400_500>=11) & (df_num.咖啡廳_400_500<=20), '咖啡廳_400_500 Class'] = 3

df_num.loc[ (df_num.咖啡廳_500_600>=0) & (df_num.咖啡廳_500_600<=5), '咖啡廳_500_600 Class'] = 1
df_num.loc[ (df_num.咖啡廳_500_600>=6) & (df_num.咖啡廳_500_600<=10), '咖啡廳_500_600 Class'] = 2
df_num.loc[ (df_num.咖啡廳_500_600>=11) & (df_num.咖啡廳_500_600<=20), '咖啡廳_500_600 Class'] = 3

df_num.loc[ (df_num.咖啡廳_600_700>=0) & (df_num.咖啡廳_600_700<=5), '咖啡廳_600_700 Class'] = 1
df_num.loc[ (df_num.咖啡廳_600_700>=6) & (df_num.咖啡廳_600_700<=10), '咖啡廳_600_700 Class'] = 2
df_num.loc[ (df_num.咖啡廳_600_700>=11) & (df_num.咖啡廳_600_700<=20), '咖啡廳_600_700 Class'] = 3

df_num.loc[ (df_num.咖啡廳_700_800>=0) & (df_num.咖啡廳_700_800<=5), '咖啡廳_700_800 Class'] = 1
df_num.loc[ (df_num.咖啡廳_700_800>=6) & (df_num.咖啡廳_700_800<=10), '咖啡廳_700_800 Class'] = 2
df_num.loc[ (df_num.咖啡廳_700_800>=11) & (df_num.咖啡廳_700_800<=20), '咖啡廳_700_800 Class'] = 3

df_num.loc[ (df_num.咖啡廳_800_900>=0) & (df_num.咖啡廳_800_900<=5), '咖啡廳_800_900 Class'] = 1
df_num.loc[ (df_num.咖啡廳_800_900>=6) & (df_num.咖啡廳_800_900<=10), '咖啡廳_800_900 Class'] = 2
df_num.loc[ (df_num.咖啡廳_800_900>=11) & (df_num.咖啡廳_800_900<=20), '咖啡廳_800_900 Class'] = 3

df_num.loc[ (df_num.咖啡廳_900_1000>=0) & (df_num.咖啡廳_900_1000<=5), '咖啡廳_900_1000 Class'] = 1
df_num.loc[ (df_num.咖啡廳_900_1000>=6) & (df_num.咖啡廳_900_1000<=10), '咖啡廳_900_1000 Class'] = 2
df_num.loc[ (df_num.咖啡廳_900_1000>=11) & (df_num.咖啡廳_900_1000<=20), '咖啡廳_900_1000 Class'] = 3

# 將便利商店做分組
df_num.loc[ (df_num.便利商店_0_100>=0) & (df_num.便利商店_0_100<=4), '便利商店_0_100 Class'] = 1
df_num.loc[ (df_num.便利商店_0_100>=5) & (df_num.便利商店_0_100<=9), '便利商店_0_100 Class'] = 2
df_num.loc[ (df_num.便利商店_0_100>=10) & (df_num.便利商店_0_100<=18), '便利商店_0_100 Class'] = 3

df_num.loc[ (df_num.便利商店_100_200>=0) & (df_num.便利商店_100_200<=4), '便利商店_100_200 Class'] = 1
df_num.loc[ (df_num.便利商店_100_200>=5) & (df_num.便利商店_100_200<=9), '便利商店_100_200 Class'] = 2
df_num.loc[ (df_num.便利商店_100_200>=10) & (df_num.便利商店_100_200<=18), '便利商店_100_200 Class'] = 3

df_num.loc[ (df_num.便利商店_200_300>=0) & (df_num.便利商店_200_300<=4), '便利商店_200_300 Class'] = 1
df_num.loc[ (df_num.便利商店_200_300>=5) & (df_num.便利商店_200_300<=9), '便利商店_200_300 Class'] = 2
df_num.loc[ (df_num.便利商店_200_300>=10) & (df_num.便利商店_200_300<=18), '便利商店_200_300 Class'] = 3

df_num.loc[ (df_num.便利商店_300_400>=0) & (df_num.便利商店_300_400<=4), '便利商店_300_400 Class'] = 1
df_num.loc[ (df_num.便利商店_300_400>=5) & (df_num.便利商店_300_400<=9), '便利商店_300_400 Class'] = 2
df_num.loc[ (df_num.便利商店_300_400>=10) & (df_num.便利商店_300_400<=18), '便利商店_300_400 Class'] = 3

df_num.loc[ (df_num.便利商店_400_500>=0) & (df_num.便利商店_400_500<=4), '便利商店_400_500 Class'] = 1
df_num.loc[ (df_num.便利商店_400_500>=5) & (df_num.便利商店_400_500<=9), '便利商店_400_500 Class'] = 2
df_num.loc[ (df_num.便利商店_400_500>=10) & (df_num.便利商店_400_500<=18), '便利商店_400_500 Class'] = 3

df_num.loc[ (df_num.便利商店_500_600>=0) & (df_num.便利商店_500_600<=4), '便利商店_500_600 Class'] = 1
df_num.loc[ (df_num.便利商店_500_600>=5) & (df_num.便利商店_500_600<=9), '便利商店_500_600 Class'] = 2
df_num.loc[ (df_num.便利商店_500_600>=10) & (df_num.便利商店_500_600<=18), '便利商店_500_600 Class'] = 3

df_num.loc[ (df_num.便利商店_600_700>=0) & (df_num.便利商店_600_700<=4), '便利商店_600_700 Class'] = 1
df_num.loc[ (df_num.便利商店_600_700>=5) & (df_num.便利商店_600_700<=9), '便利商店_600_700 Class'] = 2
df_num.loc[ (df_num.便利商店_600_700>=10) & (df_num.便利商店_600_700<=18), '便利商店_600_700 Class'] = 3

df_num.loc[ (df_num.便利商店_700_800>=0) & (df_num.便利商店_700_800<=4), '便利商店_700_800 Class'] = 1
df_num.loc[ (df_num.便利商店_700_800>=5) & (df_num.便利商店_700_800<=9), '便利商店_700_800 Class'] = 2
df_num.loc[ (df_num.便利商店_700_800>=10) & (df_num.便利商店_700_800<=18), '便利商店_700_800 Class'] = 3

df_num.loc[ (df_num.便利商店_800_900>=0) & (df_num.便利商店_800_900<=4), '便利商店_800_900 Class'] = 1
df_num.loc[ (df_num.便利商店_800_900>=5) & (df_num.便利商店_800_900<=9), '便利商店_800_900 Class'] = 2
df_num.loc[ (df_num.便利商店_800_900>=10) & (df_num.便利商店_800_900<=18), '便利商店_800_900 Class'] = 3

df_num.loc[ (df_num.便利商店_900_1000>=0) & (df_num.便利商店_900_1000<=4), '便利商店_900_1000 Class'] = 1
df_num.loc[ (df_num.便利商店_900_1000>=5) & (df_num.便利商店_900_1000<=9), '便利商店_900_1000 Class'] = 2
df_num.loc[ (df_num.便利商店_900_1000>=10) & (df_num.便利商店_900_1000<=18), '便利商店_900_1000 Class'] = 3

# 將工廠做分組
df_num.loc[ (df_num.工廠_0_100>=0) & (df_num.工廠_0_100<=1), '工廠_0_100 Class'] = 1
df_num.loc[ (df_num.工廠_0_100>=2) & (df_num.工廠_0_100<=3), '工廠_0_100 Class'] = 2
df_num.loc[ (df_num.工廠_0_100>=4) & (df_num.工廠_0_100<=6), '工廠_0_100 Class'] = 3

df_num.loc[ (df_num.工廠_100_200>=0) & (df_num.工廠_100_200<=1), '工廠_100_200 Class'] = 1
df_num.loc[ (df_num.工廠_100_200>=2) & (df_num.工廠_100_200<=3), '工廠_100_200 Class'] = 2
df_num.loc[ (df_num.工廠_100_200>=4) & (df_num.工廠_100_200<=6), '工廠_100_200 Class'] = 3

df_num.loc[ (df_num.工廠_200_300>=0) & (df_num.工廠_200_300<=1), '工廠_200_300 Class'] = 1
df_num.loc[ (df_num.工廠_200_300>=2) & (df_num.工廠_200_300<=3), '工廠_200_300 Class'] = 2
df_num.loc[ (df_num.工廠_200_300>=4) & (df_num.工廠_200_300<=6), '工廠_200_300 Class'] = 3

df_num.loc[ (df_num.工廠_300_400>=0) & (df_num.工廠_300_400<=1), '工廠_300_400 Class'] = 1
df_num.loc[ (df_num.工廠_300_400>=2) & (df_num.工廠_300_400<=3), '工廠_300_400 Class'] = 2
df_num.loc[ (df_num.工廠_300_400>=4) & (df_num.工廠_300_400<=6), '工廠_300_400 Class'] = 3

df_num.loc[ (df_num.工廠_400_500>=0) & (df_num.工廠_400_500<=1), '工廠_400_500 Class'] = 1
df_num.loc[ (df_num.工廠_400_500>=2) & (df_num.工廠_400_500<=3), '工廠_400_500 Class'] = 2
df_num.loc[ (df_num.工廠_400_500>=4) & (df_num.工廠_400_500<=6), '工廠_400_500 Class'] = 3

df_num.loc[ (df_num.工廠_500_600>=0) & (df_num.工廠_500_600<=1), '工廠_500_600 Class'] = 1
df_num.loc[ (df_num.工廠_500_600>=2) & (df_num.工廠_500_600<=3), '工廠_500_600 Class'] = 2
df_num.loc[ (df_num.工廠_500_600>=4) & (df_num.工廠_500_600<=6), '工廠_500_600 Class'] = 3

df_num.loc[ (df_num.工廠_600_700>=0) & (df_num.工廠_600_700<=1), '工廠_600_700 Class'] = 1
df_num.loc[ (df_num.工廠_600_700>=2) & (df_num.工廠_600_700<=3), '工廠_600_700 Class'] = 2
df_num.loc[ (df_num.工廠_600_700>=4) & (df_num.工廠_600_700<=6), '工廠_600_700 Class'] = 3

df_num.loc[ (df_num.工廠_700_800>=0) & (df_num.工廠_700_800<=1), '工廠_700_800 Class'] = 1
df_num.loc[ (df_num.工廠_700_800>=2) & (df_num.工廠_700_800<=3), '工廠_700_800 Class'] = 2
df_num.loc[ (df_num.工廠_700_800>=4) & (df_num.工廠_700_800<=6), '工廠_700_800 Class'] = 3

df_num.loc[ (df_num.工廠_800_900>=0) & (df_num.工廠_800_900<=1), '工廠_800_900 Class'] = 1
df_num.loc[ (df_num.工廠_800_900>=2) & (df_num.工廠_800_900<=3), '工廠_800_900 Class'] = 2
df_num.loc[ (df_num.工廠_800_900>=4) & (df_num.工廠_800_900<=6), '工廠_800_900 Class'] = 3

df_num.loc[ (df_num.工廠_900_1000>=0) & (df_num.工廠_900_1000<=1), '工廠_900_1000 Class'] = 1
df_num.loc[ (df_num.工廠_900_1000>=2) & (df_num.工廠_900_1000<=3), '工廠_900_1000 Class'] = 2
df_num.loc[ (df_num.工廠_900_1000>=4) & (df_num.工廠_900_1000<=6), '工廠_900_1000 Class'] = 3

# 將麥當勞做分組
df_num.loc[ (df_num.麥當勞_0_100>=0) & (df_num.麥當勞_0_100<=1), '麥當勞_0_100 Class'] = 1
df_num.loc[ (df_num.麥當勞_0_100==2), '麥當勞_0_100 Class'] = 2
df_num.loc[ (df_num.麥當勞_0_100>=3) & (df_num.麥當勞_0_100<=4), '麥當勞_0_100 Class'] = 3

df_num.loc[ (df_num.麥當勞_100_200>=0) & (df_num.麥當勞_100_200<=1), '麥當勞_100_200 Class'] = 1
df_num.loc[ (df_num.麥當勞_100_200==2), '麥當勞_100_200 Class'] = 2
df_num.loc[ (df_num.麥當勞_100_200>=3) & (df_num.麥當勞_100_200<=4), '麥當勞_100_200 Class'] = 3

df_num.loc[ (df_num.麥當勞_200_300>=0) & (df_num.麥當勞_200_300<=1), '麥當勞_200_300 Class'] = 1
df_num.loc[ (df_num.麥當勞_200_300==2), '麥當勞_200_300 Class'] = 2
df_num.loc[ (df_num.麥當勞_200_300>=3) & (df_num.麥當勞_200_300<=4), '麥當勞_200_300 Class'] = 3

df_num.loc[ (df_num.麥當勞_300_400>=0) & (df_num.麥當勞_300_400<=1), '麥當勞_300_400 Class'] = 1
df_num.loc[ (df_num.麥當勞_300_400==2), '麥當勞_300_400 Class'] = 2
df_num.loc[ (df_num.麥當勞_300_400>=3) & (df_num.麥當勞_300_400<=4), '麥當勞_300_400 Class'] = 3

df_num.loc[ (df_num.麥當勞_400_500>=0) & (df_num.麥當勞_400_500<=1), '麥當勞_400_500 Class'] = 1
df_num.loc[ (df_num.麥當勞_400_500==2), '麥當勞_400_500 Class'] = 2
df_num.loc[ (df_num.麥當勞_400_500>=3) & (df_num.麥當勞_400_500<=4), '麥當勞_400_500 Class'] = 3

df_num.loc[ (df_num.麥當勞_500_600>=0) & (df_num.麥當勞_500_600<=1), '麥當勞_500_600 Class'] = 1
df_num.loc[ (df_num.麥當勞_500_600==2), '麥當勞_500_600 Class'] = 2
df_num.loc[ (df_num.麥當勞_500_600>=3) & (df_num.麥當勞_500_600<=4), '麥當勞_500_600 Class'] = 3

df_num.loc[ (df_num.麥當勞_600_700>=0) & (df_num.麥當勞_600_700<=1), '麥當勞_600_700 Class'] = 1
df_num.loc[ (df_num.麥當勞_600_700==2), '麥當勞_600_700 Class'] = 2
df_num.loc[ (df_num.麥當勞_600_700>=3) & (df_num.麥當勞_600_700<=4), '麥當勞_600_700 Class'] = 3

df_num.loc[ (df_num.麥當勞_700_800>=0) & (df_num.麥當勞_700_800<=1), '麥當勞_700_800 Class'] = 1
df_num.loc[ (df_num.麥當勞_700_800==2), '麥當勞_700_800 Class'] = 2
df_num.loc[ (df_num.麥當勞_700_800>=3) & (df_num.麥當勞_700_800<=4), '麥當勞_700_800 Class'] = 3

df_num.loc[ (df_num.麥當勞_800_900>=0) & (df_num.麥當勞_800_900<=1), '麥當勞_800_900 Class'] = 1
df_num.loc[ (df_num.麥當勞_800_900==2), '麥當勞_800_900 Class'] = 2
df_num.loc[ (df_num.麥當勞_800_900>=3) & (df_num.麥當勞_800_900<=4), '麥當勞_800_900 Class'] = 3

df_num.loc[ (df_num.麥當勞_900_1000>=0) & (df_num.麥當勞_900_1000<=1), '麥當勞_900_1000 Class'] = 1
df_num.loc[ (df_num.麥當勞_900_1000==2), '麥當勞_900_1000 Class'] = 2
df_num.loc[ (df_num.麥當勞_900_1000>=3) & (df_num.麥當勞_900_1000<=4), '麥當勞_900_1000 Class'] = 3

# 將肯德基做分組
df_num.loc[ (df_num.肯德基_0_100==0), '肯德基_0_100 Class'] = 1
df_num.loc[ (df_num.肯德基_0_100==1), '肯德基_0_100 Class'] = 2
df_num.loc[ (df_num.肯德基_0_100==2), '肯德基_0_100 Class'] = 3

df_num.loc[ (df_num.肯德基_100_200==0), '肯德基_100_200 Class'] = 1
df_num.loc[ (df_num.肯德基_100_200==1), '肯德基_100_200 Class'] = 2
df_num.loc[ (df_num.肯德基_100_200==2), '肯德基_100_200 Class'] = 3

df_num.loc[ (df_num.肯德基_200_300==0), '肯德基_200_300 Class'] = 1
df_num.loc[ (df_num.肯德基_200_300==1), '肯德基_200_300 Class'] = 2
df_num.loc[ (df_num.肯德基_200_300==2), '肯德基_200_300 Class'] = 3

df_num.loc[ (df_num.肯德基_300_400==0), '肯德基_300_400 Class'] = 1
df_num.loc[ (df_num.肯德基_300_400==1), '肯德基_300_400 Class'] = 2
df_num.loc[ (df_num.肯德基_300_400==2), '肯德基_300_400 Class'] = 3

df_num.loc[ (df_num.肯德基_400_500==0), '肯德基_400_500 Class'] = 1
df_num.loc[ (df_num.肯德基_400_500==1), '肯德基_400_500 Class'] = 2
df_num.loc[ (df_num.肯德基_400_500==2), '肯德基_400_500 Class'] = 3

df_num.loc[ (df_num.肯德基_500_600==0), '肯德基_500_600 Class'] = 1
df_num.loc[ (df_num.肯德基_500_600==1), '肯德基_500_600 Class'] = 2
df_num.loc[ (df_num.肯德基_500_600==2), '肯德基_500_600 Class'] = 3

df_num.loc[ (df_num.肯德基_600_700==0), '肯德基_600_700 Class'] = 1
df_num.loc[ (df_num.肯德基_600_700==1), '肯德基_600_700 Class'] = 2
df_num.loc[ (df_num.肯德基_600_700==2), '肯德基_600_700 Class'] = 3

df_num.loc[ (df_num.肯德基_700_800==0), '肯德基_700_800 Class'] = 1
df_num.loc[ (df_num.肯德基_700_800==1), '肯德基_700_800 Class'] = 2
df_num.loc[ (df_num.肯德基_700_800==2), '肯德基_700_800 Class'] = 3

df_num.loc[ (df_num.肯德基_800_900==0), '肯德基_800_900 Class'] = 1
df_num.loc[ (df_num.肯德基_800_900==1), '肯德基_800_900 Class'] = 2
df_num.loc[ (df_num.肯德基_800_900==2), '肯德基_800_900 Class'] = 3

df_num.loc[ (df_num.肯德基_900_1000==0), '肯德基_900_1000 Class'] = 1
df_num.loc[ (df_num.肯德基_900_1000==1), '肯德基_900_1000 Class'] = 2
df_num.loc[ (df_num.肯德基_900_1000==2), '肯德基_900_1000 Class'] = 3

# 將加油站做分組
df_num.loc[ (df_num.加油站_0_100>=0) & (df_num.加油站_0_100<=1), '加油站_0_100 Class'] = 1
df_num.loc[ (df_num.加油站_0_100>=2) & (df_num.加油站_0_100<=3), '加油站_0_100 Class'] = 2
df_num.loc[ (df_num.加油站_0_100>=4) & (df_num.加油站_0_100<=5), '加油站_0_100 Class'] = 3

df_num.loc[ (df_num.加油站_100_200>=0) & (df_num.加油站_100_200<=1), '加油站_100_200 Class'] = 1
df_num.loc[ (df_num.加油站_100_200>=2) & (df_num.加油站_100_200<=3), '加油站_100_200 Class'] = 2
df_num.loc[ (df_num.加油站_100_200>=4) & (df_num.加油站_100_200<=5), '加油站_100_200 Class'] = 3

df_num.loc[ (df_num.加油站_200_300>=0) & (df_num.加油站_200_300<=1), '加油站_200_300 Class'] = 1
df_num.loc[ (df_num.加油站_200_300>=2) & (df_num.加油站_200_300<=3), '加油站_200_300 Class'] = 2
df_num.loc[ (df_num.加油站_200_300>=4) & (df_num.加油站_200_300<=5), '加油站_200_300 Class'] = 3

df_num.loc[ (df_num.加油站_300_400>=0) & (df_num.加油站_300_400<=1), '加油站_300_400 Class'] = 1
df_num.loc[ (df_num.加油站_300_400>=2) & (df_num.加油站_300_400<=3), '加油站_300_400 Class'] = 2
df_num.loc[ (df_num.加油站_300_400>=4) & (df_num.加油站_300_400<=5), '加油站_300_400 Class'] = 3

df_num.loc[ (df_num.加油站_400_500>=0) & (df_num.加油站_400_500<=1), '加油站_400_500 Class'] = 1
df_num.loc[ (df_num.加油站_400_500>=2) & (df_num.加油站_400_500<=3), '加油站_400_500 Class'] = 2
df_num.loc[ (df_num.加油站_400_500>=4) & (df_num.加油站_400_500<=5), '加油站_400_500 Class'] = 3

df_num.loc[ (df_num.加油站_500_600>=0) & (df_num.加油站_500_600<=1), '加油站_500_600 Class'] = 1
df_num.loc[ (df_num.加油站_500_600>=2) & (df_num.加油站_500_600<=3), '加油站_500_600 Class'] = 2
df_num.loc[ (df_num.加油站_500_600>=4) & (df_num.加油站_500_600<=5), '加油站_500_600 Class'] = 3

df_num.loc[ (df_num.加油站_600_700>=0) & (df_num.加油站_600_700<=1), '加油站_600_700 Class'] = 1
df_num.loc[ (df_num.加油站_600_700>=2) & (df_num.加油站_600_700<=3), '加油站_600_700 Class'] = 2
df_num.loc[ (df_num.加油站_600_700>=4) & (df_num.加油站_600_700<=5), '加油站_600_700 Class'] = 3

df_num.loc[ (df_num.加油站_700_800>=0) & (df_num.加油站_700_800<=1), '加油站_700_800 Class'] = 1
df_num.loc[ (df_num.加油站_700_800>=2) & (df_num.加油站_700_800<=3), '加油站_700_800 Class'] = 2
df_num.loc[ (df_num.加油站_700_800>=4) & (df_num.加油站_700_800<=5), '加油站_700_800 Class'] = 3

df_num.loc[ (df_num.加油站_800_900>=0) & (df_num.加油站_800_900<=1), '加油站_800_900 Class'] = 1
df_num.loc[ (df_num.加油站_800_900>=2) & (df_num.加油站_800_900<=3), '加油站_800_900 Class'] = 2
df_num.loc[ (df_num.加油站_800_900>=4) & (df_num.加油站_800_900<=5), '加油站_800_900 Class'] = 3

df_num.loc[ (df_num.加油站_900_1000>=0) & (df_num.加油站_900_1000<=1), '加油站_900_1000 Class'] = 1
df_num.loc[ (df_num.加油站_900_1000>=2) & (df_num.加油站_900_1000<=3), '加油站_900_1000 Class'] = 2
df_num.loc[ (df_num.加油站_900_1000>=4) & (df_num.加油站_900_1000<=5), '加油站_900_1000 Class'] = 3

# 將健身房做分組
df_num.loc[ (df_num.健身房_0_100>=0) & (df_num.健身房_0_100<=1), '健身房_0_100 Class'] = 1
df_num.loc[ (df_num.健身房_0_100>=2) & (df_num.健身房_0_100<=4), '健身房_0_100 Class'] = 2
df_num.loc[ (df_num.健身房_0_100>=5) & (df_num.健身房_0_100<=8), '健身房_0_100 Class'] = 3

df_num.loc[ (df_num.健身房_100_200>=0) & (df_num.健身房_100_200<=1), '健身房_100_200 Class'] = 1
df_num.loc[ (df_num.健身房_100_200>=2) & (df_num.健身房_100_200<=4), '健身房_100_200 Class'] = 2
df_num.loc[ (df_num.健身房_100_200>=5) & (df_num.健身房_100_200<=8), '健身房_100_200 Class'] = 3

df_num.loc[ (df_num.健身房_200_300>=0) & (df_num.健身房_200_300<=1), '健身房_200_300 Class'] = 1
df_num.loc[ (df_num.健身房_200_300>=2) & (df_num.健身房_200_300<=4), '健身房_200_300 Class'] = 2
df_num.loc[ (df_num.健身房_200_300>=5) & (df_num.健身房_200_300<=8), '健身房_200_300 Class'] = 3

df_num.loc[ (df_num.健身房_300_400>=0) & (df_num.健身房_300_400<=1), '健身房_300_400 Class'] = 1
df_num.loc[ (df_num.健身房_300_400>=2) & (df_num.健身房_300_400<=4), '健身房_300_400 Class'] = 2
df_num.loc[ (df_num.健身房_300_400>=5) & (df_num.健身房_300_400<=8), '健身房_300_400 Class'] = 3

df_num.loc[ (df_num.健身房_400_500>=0) & (df_num.健身房_400_500<=1), '健身房_400_500 Class'] = 1
df_num.loc[ (df_num.健身房_400_500>=2) & (df_num.健身房_400_500<=4), '健身房_400_500 Class'] = 2
df_num.loc[ (df_num.健身房_400_500>=5) & (df_num.健身房_400_500<=8), '健身房_400_500 Class'] = 3

df_num.loc[ (df_num.健身房_500_600>=0) & (df_num.健身房_500_600<=1), '健身房_500_600 Class'] = 1
df_num.loc[ (df_num.健身房_500_600>=2) & (df_num.健身房_500_600<=4), '健身房_500_600 Class'] = 2
df_num.loc[ (df_num.健身房_500_600>=5) & (df_num.健身房_500_600<=8), '健身房_500_600 Class'] = 3

df_num.loc[ (df_num.健身房_600_700>=0) & (df_num.健身房_600_700<=1), '健身房_600_700 Class'] = 1
df_num.loc[ (df_num.健身房_600_700>=2) & (df_num.健身房_600_700<=4), '健身房_600_700 Class'] = 2
df_num.loc[ (df_num.健身房_600_700>=5) & (df_num.健身房_600_700<=8), '健身房_600_700 Class'] = 3

df_num.loc[ (df_num.健身房_700_800>=0) & (df_num.健身房_700_800<=1), '健身房_700_800 Class'] = 1
df_num.loc[ (df_num.健身房_700_800>=2) & (df_num.健身房_700_800<=4), '健身房_700_800 Class'] = 2
df_num.loc[ (df_num.健身房_700_800>=5) & (df_num.健身房_700_800<=8), '健身房_700_800 Class'] = 3

df_num.loc[ (df_num.健身房_800_900>=0) & (df_num.健身房_800_900<=1), '健身房_800_900 Class'] = 1
df_num.loc[ (df_num.健身房_800_900>=2) & (df_num.健身房_800_900<=4), '健身房_800_900 Class'] = 2
df_num.loc[ (df_num.健身房_800_900>=5) & (df_num.健身房_800_900<=8), '健身房_800_900 Class'] = 3

df_num.loc[ (df_num.健身房_900_1000>=0) & (df_num.健身房_900_1000<=1), '健身房_900_1000 Class'] = 1
df_num.loc[ (df_num.健身房_900_1000>=2) & (df_num.健身房_900_1000<=4), '健身房_900_1000 Class'] = 2
df_num.loc[ (df_num.健身房_900_1000>=5) & (df_num.健身房_900_1000<=8), '健身房_900_1000 Class'] = 3

# 將國民運動中心做分組
df_num.loc[ (df_num.國民運動中心_0_100>=0) & (df_num.國民運動中心_0_100<=1), '國民運動中心_0_100 Class'] = 1
df_num.loc[ (df_num.國民運動中心_0_100==2), '國民運動中心_0_100 Class'] = 2
df_num.loc[ (df_num.國民運動中心_0_100>=3) & (df_num.國民運動中心_0_100<=4), '國民運動中心_0_100 Class'] = 3

df_num.loc[ (df_num.國民運動中心_100_200>=0) & (df_num.國民運動中心_100_200<=1), '國民運動中心_100_200 Class'] = 1
df_num.loc[ (df_num.國民運動中心_100_200==2), '國民運動中心_100_200 Class'] = 2
df_num.loc[ (df_num.國民運動中心_100_200>=3) & (df_num.國民運動中心_100_200<=4), '國民運動中心_100_200 Class'] = 3

df_num.loc[ (df_num.國民運動中心_200_300>=0) & (df_num.國民運動中心_200_300<=1), '國民運動中心_200_300 Class'] = 1
df_num.loc[ (df_num.國民運動中心_200_300==2), '國民運動中心_200_300 Class'] = 2
df_num.loc[ (df_num.國民運動中心_200_300>=3) & (df_num.國民運動中心_200_300<=4), '國民運動中心_200_300 Class'] = 3

df_num.loc[ (df_num.國民運動中心_300_400>=0) & (df_num.國民運動中心_300_400<=1), '國民運動中心_300_400 Class'] = 1
df_num.loc[ (df_num.國民運動中心_300_400==2), '國民運動中心_300_400 Class'] = 2
df_num.loc[ (df_num.國民運動中心_300_400>=3) & (df_num.國民運動中心_300_400<=4), '國民運動中心_300_400 Class'] = 3

df_num.loc[ (df_num.國民運動中心_400_500>=0) & (df_num.國民運動中心_400_500<=1), '國民運動中心_400_500 Class'] = 1
df_num.loc[ (df_num.國民運動中心_400_500==2), '國民運動中心_400_500 Class'] = 2
df_num.loc[ (df_num.國民運動中心_400_500>=3) & (df_num.國民運動中心_400_500<=4), '國民運動中心_400_500 Class'] = 3

df_num.loc[ (df_num.國民運動中心_500_600>=0) & (df_num.國民運動中心_500_600<=1), '國民運動中心_500_600 Class'] = 1
df_num.loc[ (df_num.國民運動中心_500_600==2), '國民運動中心_500_600 Class'] = 2
df_num.loc[ (df_num.國民運動中心_500_600>=3) & (df_num.國民運動中心_500_600<=4), '國民運動中心_500_600 Class'] = 3

df_num.loc[ (df_num.國民運動中心_600_700>=0) & (df_num.國民運動中心_600_700<=1), '國民運動中心_600_700 Class'] = 1
df_num.loc[ (df_num.國民運動中心_600_700==2), '國民運動中心_600_700 Class'] = 2
df_num.loc[ (df_num.國民運動中心_600_700>=3) & (df_num.國民運動中心_600_700<=4), '國民運動中心_600_700 Class'] = 3

df_num.loc[ (df_num.國民運動中心_700_800>=0) & (df_num.國民運動中心_700_800<=1), '國民運動中心_700_800 Class'] = 1
df_num.loc[ (df_num.國民運動中心_700_800==2), '國民運動中心_700_800 Class'] = 2
df_num.loc[ (df_num.國民運動中心_700_800>=3) & (df_num.國民運動中心_700_800<=4), '國民運動中心_700_800 Class'] = 3

df_num.loc[ (df_num.國民運動中心_800_900>=0) & (df_num.國民運動中心_800_900<=1), '國民運動中心_800_900 Class'] = 1
df_num.loc[ (df_num.國民運動中心_800_900==2), '國民運動中心_800_900 Class'] = 2
df_num.loc[ (df_num.國民運動中心_800_900>=3) & (df_num.國民運動中心_800_900<=4), '國民運動中心_800_900 Class'] = 3

df_num.loc[ (df_num.國民運動中心_900_1000>=0) & (df_num.國民運動中心_900_1000<=1), '國民運動中心_900_1000 Class'] = 1
df_num.loc[ (df_num.國民運動中心_900_1000==2), '國民運動中心_900_1000 Class'] = 2
df_num.loc[ (df_num.國民運動中心_900_1000>=3) & (df_num.國民運動中心_900_1000<=4), '國民運動中心_900_1000 Class'] = 3

# 將五金百貨做分組
df_num.loc[ (df_num.五金百貨_0_100>=0) & (df_num.五金百貨_0_100<=1), '五金百貨_0_100 Class'] = 1
df_num.loc[ (df_num.五金百貨_0_100==2), '五金百貨_0_100 Class'] = 2
df_num.loc[ (df_num.五金百貨_0_100>=3) & (df_num.五金百貨_0_100<=4), '五金百貨_0_100 Class'] = 3

df_num.loc[ (df_num.五金百貨_100_200>=0) & (df_num.五金百貨_100_200<=1), '五金百貨_100_200 Class'] = 1
df_num.loc[ (df_num.五金百貨_100_200==2), '五金百貨_100_200 Class'] = 2
df_num.loc[ (df_num.五金百貨_100_200>=3) & (df_num.五金百貨_100_200<=4), '五金百貨_100_200 Class'] = 3

df_num.loc[ (df_num.五金百貨_200_300>=0) & (df_num.五金百貨_200_300<=1), '五金百貨_200_300 Class'] = 1
df_num.loc[ (df_num.五金百貨_200_300==2), '五金百貨_200_300 Class'] = 2
df_num.loc[ (df_num.五金百貨_200_300>=3) & (df_num.五金百貨_200_300<=4), '五金百貨_200_300 Class'] = 3

df_num.loc[ (df_num.五金百貨_300_400>=0) & (df_num.五金百貨_300_400<=1), '五金百貨_300_400 Class'] = 1
df_num.loc[ (df_num.五金百貨_300_400==2), '五金百貨_300_400 Class'] = 2
df_num.loc[ (df_num.五金百貨_300_400>=3) & (df_num.五金百貨_300_400<=4), '五金百貨_300_400 Class'] = 3

df_num.loc[ (df_num.五金百貨_400_500>=0) & (df_num.五金百貨_400_500<=1), '五金百貨_400_500 Class'] = 1
df_num.loc[ (df_num.五金百貨_400_500==2), '五金百貨_400_500 Class'] = 2
df_num.loc[ (df_num.五金百貨_400_500>=3) & (df_num.五金百貨_400_500<=4), '五金百貨_400_500 Class'] = 3

df_num.loc[ (df_num.五金百貨_500_600>=0) & (df_num.五金百貨_500_600<=1), '五金百貨_500_600 Class'] = 1
df_num.loc[ (df_num.五金百貨_500_600==2), '五金百貨_500_600 Class'] = 2
df_num.loc[ (df_num.五金百貨_500_600>=3) & (df_num.五金百貨_500_600<=4), '五金百貨_500_600 Class'] = 3

df_num.loc[ (df_num.五金百貨_600_700>=0) & (df_num.五金百貨_600_700<=1), '五金百貨_600_700 Class'] = 1
df_num.loc[ (df_num.五金百貨_600_700==2), '五金百貨_600_700 Class'] = 2
df_num.loc[ (df_num.五金百貨_600_700>=3) & (df_num.五金百貨_600_700<=4), '五金百貨_600_700 Class'] = 3

df_num.loc[ (df_num.五金百貨_700_800>=0) & (df_num.五金百貨_700_800<=1), '五金百貨_700_800 Class'] = 1
df_num.loc[ (df_num.五金百貨_700_800==2), '五金百貨_700_800 Class'] = 2
df_num.loc[ (df_num.五金百貨_700_800>=3) & (df_num.五金百貨_700_800<=4), '五金百貨_700_800 Class'] = 3

df_num.loc[ (df_num.五金百貨_800_900>=0) & (df_num.五金百貨_800_900<=1), '五金百貨_800_900 Class'] = 1
df_num.loc[ (df_num.五金百貨_800_900==2), '五金百貨_800_900 Class'] = 2
df_num.loc[ (df_num.五金百貨_800_900>=3) & (df_num.五金百貨_800_900<=4), '五金百貨_800_900 Class'] = 3

df_num.loc[ (df_num.五金百貨_900_1000>=0) & (df_num.五金百貨_900_1000<=1), '五金百貨_900_1000 Class'] = 1
df_num.loc[ (df_num.五金百貨_900_1000==2), '五金百貨_900_1000 Class'] = 2
df_num.loc[ (df_num.五金百貨_900_1000>=3) & (df_num.五金百貨_900_1000<=4), '五金百貨_900_1000 Class'] = 3

# 將醫院做分組
df_num.loc[ (df_num.醫院_0_100>=0) & (df_num.醫院_0_100<=2), '醫院_0_100 Class'] = 1
df_num.loc[ (df_num.醫院_0_100>=3) & (df_num.醫院_0_100<=6), '醫院_0_100 Class'] = 2
df_num.loc[ (df_num.醫院_0_100>=7) & (df_num.醫院_0_100<=13), '醫院_0_100 Class'] = 3

df_num.loc[ (df_num.醫院_100_200>=0) & (df_num.醫院_100_200<=2), '醫院_100_200 Class'] = 1
df_num.loc[ (df_num.醫院_100_200>=3) & (df_num.醫院_100_200<=6), '醫院_100_200 Class'] = 2
df_num.loc[ (df_num.醫院_100_200>=7) & (df_num.醫院_100_200<=13), '醫院_100_200 Class'] = 3

df_num.loc[ (df_num.醫院_200_300>=0) & (df_num.醫院_200_300<=2), '醫院_200_300 Class'] = 1
df_num.loc[ (df_num.醫院_200_300>=3) & (df_num.醫院_200_300<=6), '醫院_200_300 Class'] = 2
df_num.loc[ (df_num.醫院_200_300>=7) & (df_num.醫院_200_300<=13), '醫院_200_300 Class'] = 3

df_num.loc[ (df_num.醫院_300_400>=0) & (df_num.醫院_300_400<=2), '醫院_300_400 Class'] = 1
df_num.loc[ (df_num.醫院_300_400>=3) & (df_num.醫院_300_400<=6), '醫院_300_400 Class'] = 2
df_num.loc[ (df_num.醫院_300_400>=7) & (df_num.醫院_300_400<=13), '醫院_300_400 Class'] = 3

df_num.loc[ (df_num.醫院_400_500>=0) & (df_num.醫院_400_500<=2), '醫院_400_500 Class'] = 1
df_num.loc[ (df_num.醫院_400_500>=3) & (df_num.醫院_400_500<=6), '醫院_400_500 Class'] = 2
df_num.loc[ (df_num.醫院_400_500>=7) & (df_num.醫院_400_500<=13), '醫院_400_500 Class'] = 3

df_num.loc[ (df_num.醫院_500_600>=0) & (df_num.醫院_500_600<=2), '醫院_500_600 Class'] = 1
df_num.loc[ (df_num.醫院_500_600>=3) & (df_num.醫院_500_600<=6), '醫院_500_600 Class'] = 2
df_num.loc[ (df_num.醫院_500_600>=7) & (df_num.醫院_500_600<=13), '醫院_500_600 Class'] = 3

df_num.loc[ (df_num.醫院_600_700>=0) & (df_num.醫院_600_700<=2), '醫院_600_700 Class'] = 1
df_num.loc[ (df_num.醫院_600_700>=3) & (df_num.醫院_600_700<=6), '醫院_600_700 Class'] = 2
df_num.loc[ (df_num.醫院_600_700>=7) & (df_num.醫院_600_700<=13), '醫院_600_700 Class'] = 3

df_num.loc[ (df_num.醫院_700_800>=0) & (df_num.醫院_700_800<=2), '醫院_700_800 Class'] = 1
df_num.loc[ (df_num.醫院_700_800>=3) & (df_num.醫院_700_800<=6), '醫院_700_800 Class'] = 2
df_num.loc[ (df_num.醫院_700_800>=7) & (df_num.醫院_700_800<=13), '醫院_700_800 Class'] = 3

df_num.loc[ (df_num.醫院_800_900>=0) & (df_num.醫院_800_900<=2), '醫院_800_900 Class'] = 1
df_num.loc[ (df_num.醫院_800_900>=3) & (df_num.醫院_800_900<=6), '醫院_800_900 Class'] = 2
df_num.loc[ (df_num.醫院_800_900>=7) & (df_num.醫院_800_900<=13), '醫院_800_900 Class'] = 3

df_num.loc[ (df_num.醫院_900_1000>=0) & (df_num.醫院_900_1000<=2), '醫院_900_1000 Class'] = 1
df_num.loc[ (df_num.醫院_900_1000>=3) & (df_num.醫院_900_1000<=6), '醫院_900_1000 Class'] = 2
df_num.loc[ (df_num.醫院_900_1000>=7) & (df_num.醫院_900_1000<=13), '醫院_900_1000 Class'] = 3

# 將診所做分組
df_num.loc[ (df_num.診所_0_100>=0) & (df_num.診所_0_100<=2), '診所_0_100 Class'] = 1
df_num.loc[ (df_num.診所_0_100>=3) & (df_num.診所_0_100<=5), '診所_0_100 Class'] = 2
df_num.loc[ (df_num.診所_0_100>=6) & (df_num.診所_0_100<=7), '診所_0_100 Class'] = 3

df_num.loc[ (df_num.診所_100_200>=0) & (df_num.診所_100_200<=2), '診所_100_200 Class'] = 1
df_num.loc[ (df_num.診所_100_200>=3) & (df_num.診所_100_200<=5), '診所_100_200 Class'] = 2
df_num.loc[ (df_num.診所_100_200>=6) & (df_num.診所_100_200<=7), '診所_100_200 Class'] = 3

df_num.loc[ (df_num.診所_200_300>=0) & (df_num.診所_200_300<=2), '診所_200_300 Class'] = 1
df_num.loc[ (df_num.診所_200_300>=3) & (df_num.診所_200_300<=5), '診所_200_300 Class'] = 2
df_num.loc[ (df_num.診所_200_300>=6) & (df_num.診所_200_300<=7), '診所_200_300 Class'] = 3

df_num.loc[ (df_num.診所_300_400>=0) & (df_num.診所_300_400<=2), '診所_300_400 Class'] = 1
df_num.loc[ (df_num.診所_300_400>=3) & (df_num.診所_300_400<=5), '診所_300_400 Class'] = 2
df_num.loc[ (df_num.診所_300_400>=6) & (df_num.診所_300_400<=7), '診所_300_400 Class'] = 3

df_num.loc[ (df_num.診所_400_500>=0) & (df_num.診所_400_500<=2), '診所_400_500 Class'] = 1
df_num.loc[ (df_num.診所_400_500>=3) & (df_num.診所_400_500<=5), '診所_400_500 Class'] = 2
df_num.loc[ (df_num.診所_400_500>=6) & (df_num.診所_400_500<=7), '診所_400_500 Class'] = 3

df_num.loc[ (df_num.診所_500_600>=0) & (df_num.診所_500_600<=2), '診所_500_600 Class'] = 1
df_num.loc[ (df_num.診所_500_600>=3) & (df_num.診所_500_600<=5), '診所_500_600 Class'] = 2
df_num.loc[ (df_num.診所_500_600>=6) & (df_num.診所_500_600<=7), '診所_500_600 Class'] = 3

df_num.loc[ (df_num.診所_600_700>=0) & (df_num.診所_600_700<=2), '診所_600_700 Class'] = 1
df_num.loc[ (df_num.診所_600_700>=3) & (df_num.診所_600_700<=5), '診所_600_700 Class'] = 2
df_num.loc[ (df_num.診所_600_700>=6) & (df_num.診所_600_700<=7), '診所_600_700 Class'] = 3

df_num.loc[ (df_num.診所_700_800>=0) & (df_num.診所_700_800<=2), '診所_700_800 Class'] = 1
df_num.loc[ (df_num.診所_700_800>=3) & (df_num.診所_700_800<=5), '診所_700_800 Class'] = 2
df_num.loc[ (df_num.診所_700_800>=6) & (df_num.診所_700_800<=7), '診所_700_800 Class'] = 3

df_num.loc[ (df_num.診所_800_900>=0) & (df_num.診所_800_900<=2), '診所_800_900 Class'] = 1
df_num.loc[ (df_num.診所_800_900>=3) & (df_num.診所_800_900<=5), '診所_800_900 Class'] = 2
df_num.loc[ (df_num.診所_800_900>=6) & (df_num.診所_800_900<=7), '診所_800_900 Class'] = 3

df_num.loc[ (df_num.診所_900_1000>=0) & (df_num.診所_900_1000<=2), '診所_900_1000 Class'] = 1
df_num.loc[ (df_num.診所_900_1000>=3) & (df_num.診所_900_1000<=5), '診所_900_1000 Class'] = 2
df_num.loc[ (df_num.診所_900_1000>=6) & (df_num.診所_900_1000<=7), '診所_900_1000 Class'] = 3

# 將圖書館做分組
df_num.loc[ (df_num.圖書館_0_100>=0) & (df_num.圖書館_0_100<=1), '圖書館_0_100 Class'] = 1
df_num.loc[ (df_num.圖書館_0_100>=2) & (df_num.圖書館_0_100<=3), '圖書館_0_100 Class'] = 2
df_num.loc[ (df_num.圖書館_0_100>=4) & (df_num.圖書館_0_100<=6), '圖書館_0_100 Class'] = 3

df_num.loc[ (df_num.圖書館_100_200>=0) & (df_num.圖書館_100_200<=1), '圖書館_100_200 Class'] = 1
df_num.loc[ (df_num.圖書館_100_200>=2) & (df_num.圖書館_100_200<=3), '圖書館_100_200 Class'] = 2
df_num.loc[ (df_num.圖書館_100_200>=4) & (df_num.圖書館_100_200<=6), '圖書館_100_200 Class'] = 3

df_num.loc[ (df_num.圖書館_200_300>=0) & (df_num.圖書館_200_300<=1), '圖書館_200_300 Class'] = 1
df_num.loc[ (df_num.圖書館_200_300>=2) & (df_num.圖書館_200_300<=3), '圖書館_200_300 Class'] = 2
df_num.loc[ (df_num.圖書館_200_300>=4) & (df_num.圖書館_200_300<=6), '圖書館_200_300 Class'] = 3

df_num.loc[ (df_num.圖書館_300_400>=0) & (df_num.圖書館_300_400<=1), '圖書館_300_400 Class'] = 1
df_num.loc[ (df_num.圖書館_300_400>=2) & (df_num.圖書館_300_400<=3), '圖書館_300_400 Class'] = 2
df_num.loc[ (df_num.圖書館_300_400>=4) & (df_num.圖書館_300_400<=6), '圖書館_300_400 Class'] = 3

df_num.loc[ (df_num.圖書館_400_500>=0) & (df_num.圖書館_400_500<=1), '圖書館_400_500 Class'] = 1
df_num.loc[ (df_num.圖書館_400_500>=2) & (df_num.圖書館_400_500<=3), '圖書館_400_500 Class'] = 2
df_num.loc[ (df_num.圖書館_400_500>=4) & (df_num.圖書館_400_500<=6), '圖書館_400_500 Class'] = 3

df_num.loc[ (df_num.圖書館_500_600>=0) & (df_num.圖書館_500_600<=1), '圖書館_500_600 Class'] = 1
df_num.loc[ (df_num.圖書館_500_600>=2) & (df_num.圖書館_500_600<=3), '圖書館_500_600 Class'] = 2
df_num.loc[ (df_num.圖書館_500_600>=4) & (df_num.圖書館_500_600<=6), '圖書館_500_600 Class'] = 3

df_num.loc[ (df_num.圖書館_600_700>=0) & (df_num.圖書館_600_700<=1), '圖書館_600_700 Class'] = 1
df_num.loc[ (df_num.圖書館_600_700>=2) & (df_num.圖書館_600_700<=3), '圖書館_600_700 Class'] = 2
df_num.loc[ (df_num.圖書館_600_700>=4) & (df_num.圖書館_600_700<=6), '圖書館_600_700 Class'] = 3

df_num.loc[ (df_num.圖書館_700_800>=0) & (df_num.圖書館_700_800<=1), '圖書館_700_800 Class'] = 1
df_num.loc[ (df_num.圖書館_700_800>=2) & (df_num.圖書館_700_800<=3), '圖書館_700_800 Class'] = 2
df_num.loc[ (df_num.圖書館_700_800>=4) & (df_num.圖書館_700_800<=6), '圖書館_700_800 Class'] = 3

df_num.loc[ (df_num.圖書館_800_900>=0) & (df_num.圖書館_800_900<=1), '圖書館_800_900 Class'] = 1
df_num.loc[ (df_num.圖書館_800_900>=2) & (df_num.圖書館_800_900<=3), '圖書館_800_900 Class'] = 2
df_num.loc[ (df_num.圖書館_800_900>=4) & (df_num.圖書館_800_900<=6), '圖書館_800_900 Class'] = 3

df_num.loc[ (df_num.圖書館_900_1000>=0) & (df_num.圖書館_900_1000<=1), '圖書館_900_1000 Class'] = 1
df_num.loc[ (df_num.圖書館_900_1000>=2) & (df_num.圖書館_900_1000<=3), '圖書館_900_1000 Class'] = 2
df_num.loc[ (df_num.圖書館_900_1000>=4) & (df_num.圖書館_900_1000<=6), '圖書館_900_1000 Class'] = 3

# 將超市做分組
df_num.loc[ (df_num.超市_0_100>=0) & (df_num.超市_0_100<=1), '超市_0_100 Class'] = 1
df_num.loc[ (df_num.超市_0_100>=2) & (df_num.超市_0_100<=3), '超市_0_100 Class'] = 2
df_num.loc[ (df_num.超市_0_100>=4) & (df_num.超市_0_100<=6), '超市_0_100 Class'] = 3

df_num.loc[ (df_num.超市_100_200>=0) & (df_num.超市_100_200<=1), '超市_100_200 Class'] = 1
df_num.loc[ (df_num.超市_100_200>=2) & (df_num.超市_100_200<=3), '超市_100_200 Class'] = 2
df_num.loc[ (df_num.超市_100_200>=4) & (df_num.超市_100_200<=6), '超市_100_200 Class'] = 3

df_num.loc[ (df_num.超市_200_300>=0) & (df_num.超市_200_300<=1), '超市_200_300 Class'] = 1
df_num.loc[ (df_num.超市_200_300>=2) & (df_num.超市_200_300<=3), '超市_200_300 Class'] = 2
df_num.loc[ (df_num.超市_200_300>=4) & (df_num.超市_200_300<=6), '超市_200_300 Class'] = 3

df_num.loc[ (df_num.超市_300_400>=0) & (df_num.超市_300_400<=1), '超市_300_400 Class'] = 1
df_num.loc[ (df_num.超市_300_400>=2) & (df_num.超市_300_400<=3), '超市_300_400 Class'] = 2
df_num.loc[ (df_num.超市_300_400>=4) & (df_num.超市_300_400<=6), '超市_300_400 Class'] = 3

df_num.loc[ (df_num.超市_400_500>=0) & (df_num.超市_400_500<=1), '超市_400_500 Class'] = 1
df_num.loc[ (df_num.超市_400_500>=2) & (df_num.超市_400_500<=3), '超市_400_500 Class'] = 2
df_num.loc[ (df_num.超市_400_500>=4) & (df_num.超市_400_500<=6), '超市_400_500 Class'] = 3

df_num.loc[ (df_num.超市_500_600>=0) & (df_num.超市_500_600<=1), '超市_500_600 Class'] = 1
df_num.loc[ (df_num.超市_500_600>=2) & (df_num.超市_500_600<=3), '超市_500_600 Class'] = 2
df_num.loc[ (df_num.超市_500_600>=4) & (df_num.超市_500_600<=6), '超市_500_600 Class'] = 3

df_num.loc[ (df_num.超市_600_700>=0) & (df_num.超市_600_700<=1), '超市_600_700 Class'] = 1
df_num.loc[ (df_num.超市_600_700>=2) & (df_num.超市_600_700<=3), '超市_600_700 Class'] = 2
df_num.loc[ (df_num.超市_600_700>=4) & (df_num.超市_600_700<=6), '超市_600_700 Class'] = 3

df_num.loc[ (df_num.超市_700_800>=0) & (df_num.超市_700_800<=1), '超市_700_800 Class'] = 1
df_num.loc[ (df_num.超市_700_800>=2) & (df_num.超市_700_800<=3), '超市_700_800 Class'] = 2
df_num.loc[ (df_num.超市_700_800>=4) & (df_num.超市_700_800<=6), '超市_700_800 Class'] = 3

df_num.loc[ (df_num.超市_800_900>=0) & (df_num.超市_800_900<=1), '超市_800_900 Class'] = 1
df_num.loc[ (df_num.超市_800_900>=2) & (df_num.超市_800_900<=3), '超市_800_900 Class'] = 2
df_num.loc[ (df_num.超市_800_900>=4) & (df_num.超市_800_900<=6), '超市_800_900 Class'] = 3

df_num.loc[ (df_num.超市_900_1000>=0) & (df_num.超市_900_1000<=1), '超市_900_1000 Class'] = 1
df_num.loc[ (df_num.超市_900_1000>=2) & (df_num.超市_900_1000<=3), '超市_900_1000 Class'] = 2
df_num.loc[ (df_num.超市_900_1000>=4) & (df_num.超市_900_1000<=6), '超市_900_1000 Class'] = 3

# 將電影院做分組
df_num.loc[ (df_num.電影院_0_100==0), '電影院_0_100 Class'] = 1
df_num.loc[ (df_num.電影院_0_100==1), '電影院_0_100 Class'] = 2
df_num.loc[ (df_num.電影院_0_100==2), '電影院_0_100 Class'] = 3

df_num.loc[ (df_num.電影院_100_200==0), '電影院_100_200 Class'] = 1
df_num.loc[ (df_num.電影院_100_200==1), '電影院_100_200 Class'] = 2
df_num.loc[ (df_num.電影院_100_200==2), '電影院_100_200 Class'] = 3

df_num.loc[ (df_num.電影院_200_300==0), '電影院_200_300 Class'] = 1
df_num.loc[ (df_num.電影院_200_300==1), '電影院_200_300 Class'] = 2
df_num.loc[ (df_num.電影院_200_300==2), '電影院_200_300 Class'] = 3

df_num.loc[ (df_num.電影院_300_400==0), '電影院_300_400 Class'] = 1
df_num.loc[ (df_num.電影院_300_400==1), '電影院_300_400 Class'] = 2
df_num.loc[ (df_num.電影院_300_400==2), '電影院_300_400 Class'] = 3

df_num.loc[ (df_num.電影院_400_500==0), '電影院_400_500 Class'] = 1
df_num.loc[ (df_num.電影院_400_500==1), '電影院_400_500 Class'] = 2
df_num.loc[ (df_num.電影院_400_500==2), '電影院_400_500 Class'] = 3

df_num.loc[ (df_num.電影院_500_600==0), '電影院_500_600 Class'] = 1
df_num.loc[ (df_num.電影院_500_600==1), '電影院_500_600 Class'] = 2
df_num.loc[ (df_num.電影院_500_600==2), '電影院_500_600 Class'] = 3

df_num.loc[ (df_num.電影院_600_700==0), '電影院_600_700 Class'] = 1
df_num.loc[ (df_num.電影院_600_700==1), '電影院_600_700 Class'] = 2
df_num.loc[ (df_num.電影院_600_700==2), '電影院_600_700 Class'] = 3

df_num.loc[ (df_num.電影院_700_800==0), '電影院_700_800 Class'] = 1
df_num.loc[ (df_num.電影院_700_800==1), '電影院_700_800 Class'] = 2
df_num.loc[ (df_num.電影院_700_800==2), '電影院_700_800 Class'] = 3

df_num.loc[ (df_num.電影院_800_900==0), '電影院_800_900 Class'] = 1
df_num.loc[ (df_num.電影院_800_900==1), '電影院_800_900 Class'] = 2
df_num.loc[ (df_num.電影院_800_900==2), '電影院_800_900 Class'] = 3

df_num.loc[ (df_num.電影院_900_1000==0), '電影院_900_1000 Class'] = 1
df_num.loc[ (df_num.電影院_900_1000==1), '電影院_900_1000 Class'] = 2
df_num.loc[ (df_num.電影院_900_1000==2), '電影院_900_1000 Class'] = 3

# 將博物館做分組
df_num.loc[ (df_num.博物館_0_100==0), '博物館_0_100 Class'] = 1
df_num.loc[ (df_num.博物館_0_100==1), '博物館_0_100 Class'] = 2
df_num.loc[ (df_num.博物館_0_100==2), '博物館_0_100 Class'] = 3

df_num.loc[ (df_num.博物館_100_200==0), '博物館_100_200 Class'] = 1
df_num.loc[ (df_num.博物館_100_200==1), '博物館_100_200 Class'] = 2
df_num.loc[ (df_num.博物館_100_200==2), '博物館_100_200 Class'] = 3

df_num.loc[ (df_num.博物館_200_300==0), '博物館_200_300 Class'] = 1
df_num.loc[ (df_num.博物館_200_300==1), '博物館_200_300 Class'] = 2
df_num.loc[ (df_num.博物館_200_300==2), '博物館_200_300 Class'] = 3

df_num.loc[ (df_num.博物館_300_400==0), '博物館_300_400 Class'] = 1
df_num.loc[ (df_num.博物館_300_400==1), '博物館_300_400 Class'] = 2
df_num.loc[ (df_num.博物館_300_400==2), '博物館_300_400 Class'] = 3

df_num.loc[ (df_num.博物館_400_500==0), '博物館_400_500 Class'] = 1
df_num.loc[ (df_num.博物館_400_500==1), '博物館_400_500 Class'] = 2
df_num.loc[ (df_num.博物館_400_500==2), '博物館_400_500 Class'] = 3

df_num.loc[ (df_num.博物館_500_600==0), '博物館_500_600 Class'] = 1
df_num.loc[ (df_num.博物館_500_600==1), '博物館_500_600 Class'] = 2
df_num.loc[ (df_num.博物館_500_600==2), '博物館_500_600 Class'] = 3

df_num.loc[ (df_num.博物館_600_700==0), '博物館_600_700 Class'] = 1
df_num.loc[ (df_num.博物館_600_700==1), '博物館_600_700 Class'] = 2
df_num.loc[ (df_num.博物館_600_700==2), '博物館_600_700 Class'] = 3

df_num.loc[ (df_num.博物館_700_800==0), '博物館_700_800 Class'] = 1
df_num.loc[ (df_num.博物館_700_800==1), '博物館_700_800 Class'] = 2
df_num.loc[ (df_num.博物館_700_800==2), '博物館_700_800 Class'] = 3

df_num.loc[ (df_num.博物館_800_900==0), '博物館_800_900 Class'] = 1
df_num.loc[ (df_num.博物館_800_900==1), '博物館_800_900 Class'] = 2
df_num.loc[ (df_num.博物館_800_900==2), '博物館_800_900 Class'] = 3

df_num.loc[ (df_num.博物館_900_1000==0), '博物館_900_1000 Class'] = 1
df_num.loc[ (df_num.博物館_900_1000==1), '博物館_900_1000 Class'] = 2
df_num.loc[ (df_num.博物館_900_1000==2), '博物館_900_1000 Class'] = 3

# 將美術館做分組
df_num.loc[ (df_num.美術館_0_100==0), '美術館_0_100 Class'] = 1
df_num.loc[ (df_num.美術館_0_100==1), '美術館_0_100 Class'] = 2
df_num.loc[ (df_num.美術館_0_100>=2) & (df_num.美術館_0_100<=3), '美術館_0_100 Class'] = 3

df_num.loc[ (df_num.美術館_100_200==0), '美術館_100_200 Class'] = 1
df_num.loc[ (df_num.美術館_100_200==1), '美術館_100_200 Class'] = 2
df_num.loc[ (df_num.美術館_100_200>=2) & (df_num.美術館_100_200<=3), '美術館_100_200 Class'] = 3

df_num.loc[ (df_num.美術館_200_300==0), '美術館_200_300 Class'] = 1
df_num.loc[ (df_num.美術館_200_300==1), '美術館_200_300 Class'] = 2
df_num.loc[ (df_num.美術館_200_300>=2) & (df_num.美術館_200_300<=3), '美術館_200_300 Class'] = 3

df_num.loc[ (df_num.美術館_300_400==0), '美術館_300_400 Class'] = 1
df_num.loc[ (df_num.美術館_300_400==1), '美術館_300_400 Class'] = 2
df_num.loc[ (df_num.美術館_300_400>=2) & (df_num.美術館_300_400<=3), '美術館_300_400 Class'] = 3

df_num.loc[ (df_num.美術館_400_500==0), '美術館_400_500 Class'] = 1
df_num.loc[ (df_num.美術館_400_500==1), '美術館_400_500 Class'] = 2
df_num.loc[ (df_num.美術館_400_500>=2) & (df_num.美術館_400_500<=3), '美術館_400_500 Class'] = 3

df_num.loc[ (df_num.美術館_500_600==0), '美術館_500_600 Class'] = 1
df_num.loc[ (df_num.美術館_500_600==1), '美術館_500_600 Class'] = 2
df_num.loc[ (df_num.美術館_500_600>=2) & (df_num.美術館_500_600<=3), '美術館_500_600 Class'] = 3

df_num.loc[ (df_num.美術館_600_700==0), '美術館_600_700 Class'] = 1
df_num.loc[ (df_num.美術館_600_700==1), '美術館_600_700 Class'] = 2
df_num.loc[ (df_num.美術館_600_700>=2) & (df_num.美術館_600_700<=3), '美術館_600_700 Class'] = 3

df_num.loc[ (df_num.美術館_700_800==0), '美術館_700_800 Class'] = 1
df_num.loc[ (df_num.美術館_700_800==1), '美術館_700_800 Class'] = 2
df_num.loc[ (df_num.美術館_700_800>=2) & (df_num.美術館_700_800<=3), '美術館_700_800 Class'] = 3

df_num.loc[ (df_num.美術館_800_900==0), '美術館_800_900 Class'] = 1
df_num.loc[ (df_num.美術館_800_900==1), '美術館_800_900 Class'] = 2
df_num.loc[ (df_num.美術館_800_900>=2) & (df_num.美術館_800_900<=3), '美術館_800_900 Class'] = 3

df_num.loc[ (df_num.美術館_900_1000==0), '美術館_900_1000 Class'] = 1
df_num.loc[ (df_num.美術館_900_1000==1), '美術館_900_1000 Class'] = 2
df_num.loc[ (df_num.美術館_900_1000>=2) & (df_num.美術館_900_1000<=3), '美術館_900_1000 Class'] = 3

# 將夜市做分組
df_num.loc[ (df_num.夜市_0_100>=0) & (df_num.夜市_0_100<=2), '夜市_0_100 Class'] = 1
df_num.loc[ (df_num.夜市_0_100>=3) & (df_num.夜市_0_100<=5), '夜市_0_100 Class'] = 2
df_num.loc[ (df_num.夜市_0_100>=6) & (df_num.夜市_0_100<=15), '夜市_0_100 Class'] = 3

df_num.loc[ (df_num.夜市_100_200>=0) & (df_num.夜市_100_200<=2), '夜市_100_200 Class'] = 1
df_num.loc[ (df_num.夜市_100_200>=3) & (df_num.夜市_100_200<=5), '夜市_100_200 Class'] = 2
df_num.loc[ (df_num.夜市_100_200>=6) & (df_num.夜市_100_200<=15), '夜市_100_200 Class'] = 3

df_num.loc[ (df_num.夜市_200_300>=0) & (df_num.夜市_200_300<=2), '夜市_200_300 Class'] = 1
df_num.loc[ (df_num.夜市_200_300>=3) & (df_num.夜市_200_300<=5), '夜市_200_300 Class'] = 2
df_num.loc[ (df_num.夜市_200_300>=6) & (df_num.夜市_200_300<=15), '夜市_200_300 Class'] = 3

df_num.loc[ (df_num.夜市_300_400>=0) & (df_num.夜市_300_400<=2), '夜市_300_400 Class'] = 1
df_num.loc[ (df_num.夜市_300_400>=3) & (df_num.夜市_300_400<=5), '夜市_300_400 Class'] = 2
df_num.loc[ (df_num.夜市_300_400>=6) & (df_num.夜市_300_400<=15), '夜市_300_400 Class'] = 3

df_num.loc[ (df_num.夜市_400_500>=0) & (df_num.夜市_400_500<=2), '夜市_400_500 Class'] = 1
df_num.loc[ (df_num.夜市_400_500>=3) & (df_num.夜市_400_500<=5), '夜市_400_500 Class'] = 2
df_num.loc[ (df_num.夜市_400_500>=6) & (df_num.夜市_400_500<=15), '夜市_400_500 Class'] = 3

df_num.loc[ (df_num.夜市_500_600>=0) & (df_num.夜市_500_600<=2), '夜市_500_600 Class'] = 1
df_num.loc[ (df_num.夜市_500_600>=3) & (df_num.夜市_500_600<=5), '夜市_500_600 Class'] = 2
df_num.loc[ (df_num.夜市_500_600>=6) & (df_num.夜市_500_600<=15), '夜市_500_600 Class'] = 3

df_num.loc[ (df_num.夜市_600_700>=0) & (df_num.夜市_600_700<=2), '夜市_600_700 Class'] = 1
df_num.loc[ (df_num.夜市_600_700>=3) & (df_num.夜市_600_700<=5), '夜市_600_700 Class'] = 2
df_num.loc[ (df_num.夜市_600_700>=6) & (df_num.夜市_600_700<=15), '夜市_600_700 Class'] = 3

df_num.loc[ (df_num.夜市_700_800>=0) & (df_num.夜市_700_800<=2), '夜市_700_800 Class'] = 1
df_num.loc[ (df_num.夜市_700_800>=3) & (df_num.夜市_700_800<=5), '夜市_700_800 Class'] = 2
df_num.loc[ (df_num.夜市_700_800>=6) & (df_num.夜市_700_800<=15), '夜市_700_800 Class'] = 3

df_num.loc[ (df_num.夜市_800_900>=0) & (df_num.夜市_800_900<=2), '夜市_800_900 Class'] = 1
df_num.loc[ (df_num.夜市_800_900>=3) & (df_num.夜市_800_900<=5), '夜市_800_900 Class'] = 2
df_num.loc[ (df_num.夜市_800_900>=6) & (df_num.夜市_800_900<=15), '夜市_800_900 Class'] = 3

df_num.loc[ (df_num.夜市_900_1000>=0) & (df_num.夜市_900_1000<=2), '夜市_900_1000 Class'] = 1
df_num.loc[ (df_num.夜市_900_1000>=3) & (df_num.夜市_900_1000<=5), '夜市_900_1000 Class'] = 2
df_num.loc[ (df_num.夜市_900_1000>=6) & (df_num.夜市_900_1000<=15), '夜市_900_1000 Class'] = 3

# 將公園做分組
df_num.loc[ (df_num.公園_0_100>=0) & (df_num.公園_0_100<=2), '公園_0_100 Class'] = 1
df_num.loc[ (df_num.公園_0_100>=3) & (df_num.公園_0_100<=6), '公園_0_100 Class'] = 2
df_num.loc[ (df_num.公園_0_100>=7) & (df_num.公園_0_100<=9), '公園_0_100 Class'] = 3

df_num.loc[ (df_num.公園_100_200>=0) & (df_num.公園_100_200<=2), '公園_100_200 Class'] = 1
df_num.loc[ (df_num.公園_100_200>=3) & (df_num.公園_100_200<=6), '公園_100_200 Class'] = 2
df_num.loc[ (df_num.公園_100_200>=7) & (df_num.公園_100_200<=9), '公園_100_200 Class'] = 3

df_num.loc[ (df_num.公園_200_300>=0) & (df_num.公園_200_300<=2), '公園_200_300 Class'] = 1
df_num.loc[ (df_num.公園_200_300>=3) & (df_num.公園_200_300<=6), '公園_200_300 Class'] = 2
df_num.loc[ (df_num.公園_200_300>=7) & (df_num.公園_200_300<=9), '公園_200_300 Class'] = 3

df_num.loc[ (df_num.公園_300_400>=0) & (df_num.公園_300_400<=2), '公園_300_400 Class'] = 1
df_num.loc[ (df_num.公園_300_400>=3) & (df_num.公園_300_400<=6), '公園_300_400 Class'] = 2
df_num.loc[ (df_num.公園_300_400>=7) & (df_num.公園_300_400<=9), '公園_300_400 Class'] = 3

df_num.loc[ (df_num.公園_400_500>=0) & (df_num.公園_400_500<=2), '公園_400_500 Class'] = 1
df_num.loc[ (df_num.公園_400_500>=3) & (df_num.公園_400_500<=6), '公園_400_500 Class'] = 2
df_num.loc[ (df_num.公園_400_500>=7) & (df_num.公園_400_500<=9), '公園_400_500 Class'] = 3

df_num.loc[ (df_num.公園_500_600>=0) & (df_num.公園_500_600<=2), '公園_500_600 Class'] = 1
df_num.loc[ (df_num.公園_500_600>=3) & (df_num.公園_500_600<=6), '公園_500_600 Class'] = 2
df_num.loc[ (df_num.公園_500_600>=7) & (df_num.公園_500_600<=9), '公園_500_600 Class'] = 3

df_num.loc[ (df_num.公園_600_700>=0) & (df_num.公園_600_700<=2), '公園_600_700 Class'] = 1
df_num.loc[ (df_num.公園_600_700>=3) & (df_num.公園_600_700<=6), '公園_600_700 Class'] = 2
df_num.loc[ (df_num.公園_600_700>=7) & (df_num.公園_600_700<=9), '公園_600_700 Class'] = 3

df_num.loc[ (df_num.公園_700_800>=0) & (df_num.公園_700_800<=2), '公園_700_800 Class'] = 1
df_num.loc[ (df_num.公園_700_800>=3) & (df_num.公園_700_800<=6), '公園_700_800 Class'] = 2
df_num.loc[ (df_num.公園_700_800>=7) & (df_num.公園_700_800<=9), '公園_700_800 Class'] = 3

df_num.loc[ (df_num.公園_800_900>=0) & (df_num.公園_800_900<=2), '公園_800_900 Class'] = 1
df_num.loc[ (df_num.公園_800_900>=3) & (df_num.公園_800_900<=6), '公園_800_900 Class'] = 2
df_num.loc[ (df_num.公園_800_900>=7) & (df_num.公園_800_900<=9), '公園_800_900 Class'] = 3

df_num.loc[ (df_num.公園_900_1000>=0) & (df_num.公園_900_1000<=2), '公園_900_1000 Class'] = 1
df_num.loc[ (df_num.公園_900_1000>=3) & (df_num.公園_900_1000<=6), '公園_900_1000 Class'] = 2
df_num.loc[ (df_num.公園_900_1000>=7) & (df_num.公園_900_1000<=9), '公園_900_1000 Class'] = 3

# 將停車場做分組
df_num.loc[ (df_num.停車場_0_100>=0) & (df_num.停車場_0_100<=4), '停車場_0_100 Class'] = 1
df_num.loc[ (df_num.停車場_0_100>=5) & (df_num.停車場_0_100<=9), '停車場_0_100 Class'] = 2
df_num.loc[ (df_num.停車場_0_100>=10) & (df_num.停車場_0_100<=17), '停車場_0_100 Class'] = 3

df_num.loc[ (df_num.停車場_100_200>=0) & (df_num.停車場_100_200<=4), '停車場_100_200 Class'] = 1
df_num.loc[ (df_num.停車場_100_200>=5) & (df_num.停車場_100_200<=9), '停車場_100_200 Class'] = 2
df_num.loc[ (df_num.停車場_100_200>=10) & (df_num.停車場_100_200<=17), '停車場_100_200 Class'] = 3

df_num.loc[ (df_num.停車場_200_300>=0) & (df_num.停車場_200_300<=4), '停車場_200_300 Class'] = 1
df_num.loc[ (df_num.停車場_200_300>=5) & (df_num.停車場_200_300<=9), '停車場_200_300 Class'] = 2
df_num.loc[ (df_num.停車場_200_300>=10) & (df_num.停車場_200_300<=17), '停車場_200_300 Class'] = 3

df_num.loc[ (df_num.停車場_300_400>=0) & (df_num.停車場_300_400<=4), '停車場_300_400 Class'] = 1
df_num.loc[ (df_num.停車場_300_400>=5) & (df_num.停車場_300_400<=9), '停車場_300_400 Class'] = 2
df_num.loc[ (df_num.停車場_300_400>=10) & (df_num.停車場_300_400<=17), '停車場_300_400 Class'] = 3

df_num.loc[ (df_num.停車場_400_500>=0) & (df_num.停車場_400_500<=4), '停車場_400_500 Class'] = 1
df_num.loc[ (df_num.停車場_400_500>=5) & (df_num.停車場_400_500<=9), '停車場_400_500 Class'] = 2
df_num.loc[ (df_num.停車場_400_500>=10) & (df_num.停車場_400_500<=17), '停車場_400_500 Class'] = 3

df_num.loc[ (df_num.停車場_500_600>=0) & (df_num.停車場_500_600<=4), '停車場_500_600 Class'] = 1
df_num.loc[ (df_num.停車場_500_600>=5) & (df_num.停車場_500_600<=9), '停車場_500_600 Class'] = 2
df_num.loc[ (df_num.停車場_500_600>=10) & (df_num.停車場_500_600<=17), '停車場_500_600 Class'] = 3

df_num.loc[ (df_num.停車場_600_700>=0) & (df_num.停車場_600_700<=4), '停車場_600_700 Class'] = 1
df_num.loc[ (df_num.停車場_600_700>=5) & (df_num.停車場_600_700<=9), '停車場_600_700 Class'] = 2
df_num.loc[ (df_num.停車場_600_700>=10) & (df_num.停車場_600_700<=17), '停車場_600_700 Class'] = 3

df_num.loc[ (df_num.停車場_700_800>=0) & (df_num.停車場_700_800<=4), '停車場_700_800 Class'] = 1
df_num.loc[ (df_num.停車場_700_800>=5) & (df_num.停車場_700_800<=9), '停車場_700_800 Class'] = 2
df_num.loc[ (df_num.停車場_700_800>=10) & (df_num.停車場_700_800<=17), '停車場_700_800 Class'] = 3

df_num.loc[ (df_num.停車場_800_900>=0) & (df_num.停車場_800_900<=4), '停車場_800_900 Class'] = 1
df_num.loc[ (df_num.停車場_800_900>=5) & (df_num.停車場_800_900<=9), '停車場_800_900 Class'] = 2
df_num.loc[ (df_num.停車場_800_900>=10) & (df_num.停車場_800_900<=17), '停車場_800_900 Class'] = 3

df_num.loc[ (df_num.停車場_900_1000>=0) & (df_num.停車場_900_1000<=4), '停車場_900_1000 Class'] = 1
df_num.loc[ (df_num.停車場_900_1000>=5) & (df_num.停車場_900_1000<=9), '停車場_900_1000 Class'] = 2
df_num.loc[ (df_num.停車場_900_1000>=10) & (df_num.停車場_900_1000<=17), '停車場_900_1000 Class'] = 3

# 將餐廳做分組
df_num.loc[ (df_num.餐廳_0_100>=0) & (df_num.餐廳_0_100<=5), '餐廳_0_100 Class'] = 1
df_num.loc[ (df_num.餐廳_0_100>=6) & (df_num.餐廳_0_100<=10), '餐廳_0_100 Class'] = 2
df_num.loc[ (df_num.餐廳_0_100>=11) & (df_num.餐廳_0_100<=20), '餐廳_0_100 Class'] = 3

df_num.loc[ (df_num.餐廳_100_200>=0) & (df_num.餐廳_100_200<=5), '餐廳_100_200 Class'] = 1
df_num.loc[ (df_num.餐廳_100_200>=6) & (df_num.餐廳_100_200<=10), '餐廳_100_200 Class'] = 2
df_num.loc[ (df_num.餐廳_100_200>=11) & (df_num.餐廳_100_200<=20), '餐廳_100_200 Class'] = 3

df_num.loc[ (df_num.餐廳_200_300>=0) & (df_num.餐廳_200_300<=5), '餐廳_200_300 Class'] = 1
df_num.loc[ (df_num.餐廳_200_300>=6) & (df_num.餐廳_200_300<=10), '餐廳_200_300 Class'] = 2
df_num.loc[ (df_num.餐廳_200_300>=11) & (df_num.餐廳_200_300<=20), '餐廳_200_300 Class'] = 3

df_num.loc[ (df_num.餐廳_300_400>=0) & (df_num.餐廳_300_400<=5), '餐廳_300_400 Class'] = 1
df_num.loc[ (df_num.餐廳_300_400>=6) & (df_num.餐廳_300_400<=10), '餐廳_300_400 Class'] = 2
df_num.loc[ (df_num.餐廳_300_400>=11) & (df_num.餐廳_300_400<=20), '餐廳_300_400 Class'] = 3

df_num.loc[ (df_num.餐廳_400_500>=0) & (df_num.餐廳_400_500<=5), '餐廳_400_500 Class'] = 1
df_num.loc[ (df_num.餐廳_400_500>=6) & (df_num.餐廳_400_500<=10), '餐廳_400_500 Class'] = 2
df_num.loc[ (df_num.餐廳_400_500>=11) & (df_num.餐廳_400_500<=20), '餐廳_400_500 Class'] = 3

df_num.loc[ (df_num.餐廳_500_600>=0) & (df_num.餐廳_500_600<=5), '餐廳_500_600 Class'] = 1
df_num.loc[ (df_num.餐廳_500_600>=6) & (df_num.餐廳_500_600<=10), '餐廳_500_600 Class'] = 2
df_num.loc[ (df_num.餐廳_500_600>=11) & (df_num.餐廳_500_600<=20), '餐廳_500_600 Class'] = 3

df_num.loc[ (df_num.餐廳_600_700>=0) & (df_num.餐廳_600_700<=5), '餐廳_600_700 Class'] = 1
df_num.loc[ (df_num.餐廳_600_700>=6) & (df_num.餐廳_600_700<=10), '餐廳_600_700 Class'] = 2
df_num.loc[ (df_num.餐廳_600_700>=11) & (df_num.餐廳_600_700<=20), '餐廳_600_700 Class'] = 3

df_num.loc[ (df_num.餐廳_700_800>=0) & (df_num.餐廳_700_800<=5), '餐廳_700_800 Class'] = 1
df_num.loc[ (df_num.餐廳_700_800>=6) & (df_num.餐廳_700_800<=10), '餐廳_700_800 Class'] = 2
df_num.loc[ (df_num.餐廳_700_800>=11) & (df_num.餐廳_700_800<=20), '餐廳_700_800 Class'] = 3

df_num.loc[ (df_num.餐廳_800_900>=0) & (df_num.餐廳_800_900<=5), '餐廳_800_900 Class'] = 1
df_num.loc[ (df_num.餐廳_800_900>=6) & (df_num.餐廳_800_900<=10), '餐廳_800_900 Class'] = 2
df_num.loc[ (df_num.餐廳_800_900>=11) & (df_num.餐廳_800_900<=20), '餐廳_800_900 Class'] = 3

df_num.loc[ (df_num.餐廳_900_1000>=0) & (df_num.餐廳_900_1000<=5), '餐廳_900_1000 Class'] = 1
df_num.loc[ (df_num.餐廳_900_1000>=6) & (df_num.餐廳_900_1000<=10), '餐廳_900_1000 Class'] = 2
df_num.loc[ (df_num.餐廳_900_1000>=11) & (df_num.餐廳_900_1000<=20), '餐廳_900_1000 Class'] = 3

# 將景點做分組
df_num.loc[ (df_num.景點_0_100>=0) & (df_num.景點_0_100<=1), '景點_0_100 Class'] = 1
df_num.loc[ (df_num.景點_0_100>=2) & (df_num.景點_0_100<=3), '景點_0_100 Class'] = 2
df_num.loc[ (df_num.景點_0_100>=4) & (df_num.景點_0_100<=6), '景點_0_100 Class'] = 3

df_num.loc[ (df_num.景點_100_200>=0) & (df_num.景點_100_200<=1), '景點_100_200 Class'] = 1
df_num.loc[ (df_num.景點_100_200>=2) & (df_num.景點_100_200<=3), '景點_100_200 Class'] = 2
df_num.loc[ (df_num.景點_100_200>=4) & (df_num.景點_100_200<=6), '景點_100_200 Class'] = 3

df_num.loc[ (df_num.景點_200_300>=0) & (df_num.景點_200_300<=1), '景點_200_300 Class'] = 1
df_num.loc[ (df_num.景點_200_300>=2) & (df_num.景點_200_300<=3), '景點_200_300 Class'] = 2
df_num.loc[ (df_num.景點_200_300>=4) & (df_num.景點_200_300<=6), '景點_200_300 Class'] = 3

df_num.loc[ (df_num.景點_300_400>=0) & (df_num.景點_300_400<=1), '景點_300_400 Class'] = 1
df_num.loc[ (df_num.景點_300_400>=2) & (df_num.景點_300_400<=3), '景點_300_400 Class'] = 2
df_num.loc[ (df_num.景點_300_400>=4) & (df_num.景點_300_400<=6), '景點_300_400 Class'] = 3

df_num.loc[ (df_num.景點_400_500>=0) & (df_num.景點_400_500<=1), '景點_400_500 Class'] = 1
df_num.loc[ (df_num.景點_400_500>=2) & (df_num.景點_400_500<=3), '景點_400_500 Class'] = 2
df_num.loc[ (df_num.景點_400_500>=4) & (df_num.景點_400_500<=6), '景點_400_500 Class'] = 3

df_num.loc[ (df_num.景點_500_600>=0) & (df_num.景點_500_600<=1), '景點_500_600 Class'] = 1
df_num.loc[ (df_num.景點_500_600>=2) & (df_num.景點_500_600<=3), '景點_500_600 Class'] = 2
df_num.loc[ (df_num.景點_500_600>=4) & (df_num.景點_500_600<=6), '景點_500_600 Class'] = 3

df_num.loc[ (df_num.景點_600_700>=0) & (df_num.景點_600_700<=1), '景點_600_700 Class'] = 1
df_num.loc[ (df_num.景點_600_700>=2) & (df_num.景點_600_700<=3), '景點_600_700 Class'] = 2
df_num.loc[ (df_num.景點_600_700>=4) & (df_num.景點_600_700<=6), '景點_600_700 Class'] = 3

df_num.loc[ (df_num.景點_700_800>=0) & (df_num.景點_700_800<=1), '景點_700_800 Class'] = 1
df_num.loc[ (df_num.景點_700_800>=2) & (df_num.景點_700_800<=3), '景點_700_800 Class'] = 2
df_num.loc[ (df_num.景點_700_800>=4) & (df_num.景點_700_800<=6), '景點_700_800 Class'] = 3

df_num.loc[ (df_num.景點_800_900>=0) & (df_num.景點_800_900<=1), '景點_800_900 Class'] = 1
df_num.loc[ (df_num.景點_800_900>=2) & (df_num.景點_800_900<=3), '景點_800_900 Class'] = 2
df_num.loc[ (df_num.景點_800_900>=4) & (df_num.景點_800_900<=6), '景點_800_900 Class'] = 3

df_num.loc[ (df_num.景點_900_1000>=0) & (df_num.景點_900_1000<=1), '景點_900_1000 Class'] = 1
df_num.loc[ (df_num.景點_900_1000>=2) & (df_num.景點_900_1000<=3), '景點_900_1000 Class'] = 2
df_num.loc[ (df_num.景點_900_1000>=4) & (df_num.景點_900_1000<=6), '景點_900_1000 Class'] = 3

# 將幼稚園做分組
df_num.loc[ (df_num.幼稚園_0_100>=0) & (df_num.幼稚園_0_100<=2), '幼稚園_0_100 Class'] = 1
df_num.loc[ (df_num.幼稚園_0_100>=3) & (df_num.幼稚園_0_100<=6), '幼稚園_0_100 Class'] = 2
df_num.loc[ (df_num.幼稚園_0_100>=7) & (df_num.幼稚園_0_100<=9), '幼稚園_0_100 Class'] = 3

df_num.loc[ (df_num.幼稚園_100_200>=0) & (df_num.幼稚園_100_200<=2), '幼稚園_100_200 Class'] = 1
df_num.loc[ (df_num.幼稚園_100_200>=3) & (df_num.幼稚園_100_200<=6), '幼稚園_100_200 Class'] = 2
df_num.loc[ (df_num.幼稚園_100_200>=7) & (df_num.幼稚園_100_200<=9), '幼稚園_100_200 Class'] = 3

df_num.loc[ (df_num.幼稚園_200_300>=0) & (df_num.幼稚園_200_300<=2), '幼稚園_200_300 Class'] = 1
df_num.loc[ (df_num.幼稚園_200_300>=3) & (df_num.幼稚園_200_300<=6), '幼稚園_200_300 Class'] = 2
df_num.loc[ (df_num.幼稚園_200_300>=7) & (df_num.幼稚園_200_300<=9), '幼稚園_200_300 Class'] = 3

df_num.loc[ (df_num.幼稚園_300_400>=0) & (df_num.幼稚園_300_400<=2), '幼稚園_300_400 Class'] = 1
df_num.loc[ (df_num.幼稚園_300_400>=3) & (df_num.幼稚園_300_400<=6), '幼稚園_300_400 Class'] = 2
df_num.loc[ (df_num.幼稚園_300_400>=7) & (df_num.幼稚園_300_400<=9), '幼稚園_300_400 Class'] = 3

df_num.loc[ (df_num.幼稚園_400_500>=0) & (df_num.幼稚園_400_500<=2), '幼稚園_400_500 Class'] = 1
df_num.loc[ (df_num.幼稚園_400_500>=3) & (df_num.幼稚園_400_500<=6), '幼稚園_400_500 Class'] = 2
df_num.loc[ (df_num.幼稚園_400_500>=7) & (df_num.幼稚園_400_500<=9), '幼稚園_400_500 Class'] = 3

df_num.loc[ (df_num.幼稚園_500_600>=0) & (df_num.幼稚園_500_600<=2), '幼稚園_500_600 Class'] = 1
df_num.loc[ (df_num.幼稚園_500_600>=3) & (df_num.幼稚園_500_600<=6), '幼稚園_500_600 Class'] = 2
df_num.loc[ (df_num.幼稚園_500_600>=7) & (df_num.幼稚園_500_600<=9), '幼稚園_500_600 Class'] = 3

df_num.loc[ (df_num.幼稚園_600_700>=0) & (df_num.幼稚園_600_700<=2), '幼稚園_600_700 Class'] = 1
df_num.loc[ (df_num.幼稚園_600_700>=3) & (df_num.幼稚園_600_700<=6), '幼稚園_600_700 Class'] = 2
df_num.loc[ (df_num.幼稚園_600_700>=7) & (df_num.幼稚園_600_700<=9), '幼稚園_600_700 Class'] = 3

df_num.loc[ (df_num.幼稚園_700_800>=0) & (df_num.幼稚園_700_800<=2), '幼稚園_700_800 Class'] = 1
df_num.loc[ (df_num.幼稚園_700_800>=3) & (df_num.幼稚園_700_800<=6), '幼稚園_700_800 Class'] = 2
df_num.loc[ (df_num.幼稚園_700_800>=7) & (df_num.幼稚園_700_800<=9), '幼稚園_700_800 Class'] = 3

df_num.loc[ (df_num.幼稚園_800_900>=0) & (df_num.幼稚園_800_900<=2), '幼稚園_800_900 Class'] = 1
df_num.loc[ (df_num.幼稚園_800_900>=3) & (df_num.幼稚園_800_900<=6), '幼稚園_800_900 Class'] = 2
df_num.loc[ (df_num.幼稚園_800_900>=7) & (df_num.幼稚園_800_900<=9), '幼稚園_800_900 Class'] = 3

df_num.loc[ (df_num.幼稚園_900_1000>=0) & (df_num.幼稚園_900_1000<=2), '幼稚園_900_1000 Class'] = 1
df_num.loc[ (df_num.幼稚園_900_1000>=3) & (df_num.幼稚園_900_1000<=6), '幼稚園_900_1000 Class'] = 2
df_num.loc[ (df_num.幼稚園_900_1000>=7) & (df_num.幼稚園_900_1000<=9), '幼稚園_900_1000 Class'] = 3

# 將國小做分組
df_num.loc[ (df_num.國小_0_100>=0) & (df_num.國小_0_100<=1), '國小_0_100 Class'] = 1
df_num.loc[ (df_num.國小_0_100>=2) & (df_num.國小_0_100<=3), '國小_0_100 Class'] = 2
df_num.loc[ (df_num.國小_0_100>=4) & (df_num.國小_0_100<=6), '國小_0_100 Class'] = 3

df_num.loc[ (df_num.國小_100_200>=0) & (df_num.國小_100_200<=1), '國小_100_200 Class'] = 1
df_num.loc[ (df_num.國小_100_200>=2) & (df_num.國小_100_200<=3), '國小_100_200 Class'] = 2
df_num.loc[ (df_num.國小_100_200>=4) & (df_num.國小_100_200<=6), '國小_100_200 Class'] = 3

df_num.loc[ (df_num.國小_200_300>=0) & (df_num.國小_200_300<=1), '國小_200_300 Class'] = 1
df_num.loc[ (df_num.國小_200_300>=2) & (df_num.國小_200_300<=3), '國小_200_300 Class'] = 2
df_num.loc[ (df_num.國小_200_300>=4) & (df_num.國小_200_300<=6), '國小_200_300 Class'] = 3

df_num.loc[ (df_num.國小_300_400>=0) & (df_num.國小_300_400<=1), '國小_300_400 Class'] = 1
df_num.loc[ (df_num.國小_300_400>=2) & (df_num.國小_300_400<=3), '國小_300_400 Class'] = 2
df_num.loc[ (df_num.國小_300_400>=4) & (df_num.國小_300_400<=6), '國小_300_400 Class'] = 3

df_num.loc[ (df_num.國小_400_500>=0) & (df_num.國小_400_500<=1), '國小_400_500 Class'] = 1
df_num.loc[ (df_num.國小_400_500>=2) & (df_num.國小_400_500<=3), '國小_400_500 Class'] = 2
df_num.loc[ (df_num.國小_400_500>=4) & (df_num.國小_400_500<=6), '國小_400_500 Class'] = 3

df_num.loc[ (df_num.國小_500_600>=0) & (df_num.國小_500_600<=1), '國小_500_600 Class'] = 1
df_num.loc[ (df_num.國小_500_600>=2) & (df_num.國小_500_600<=3), '國小_500_600 Class'] = 2
df_num.loc[ (df_num.國小_500_600>=4) & (df_num.國小_500_600<=6), '國小_500_600 Class'] = 3

df_num.loc[ (df_num.國小_600_700>=0) & (df_num.國小_600_700<=1), '國小_600_700 Class'] = 1
df_num.loc[ (df_num.國小_600_700>=2) & (df_num.國小_600_700<=3), '國小_600_700 Class'] = 2
df_num.loc[ (df_num.國小_600_700>=4) & (df_num.國小_600_700<=6), '國小_600_700 Class'] = 3

df_num.loc[ (df_num.國小_700_800>=0) & (df_num.國小_700_800<=1), '國小_700_800 Class'] = 1
df_num.loc[ (df_num.國小_700_800>=2) & (df_num.國小_700_800<=3), '國小_700_800 Class'] = 2
df_num.loc[ (df_num.國小_700_800>=4) & (df_num.國小_700_800<=6), '國小_700_800 Class'] = 3

df_num.loc[ (df_num.國小_800_900>=0) & (df_num.國小_800_900<=1), '國小_800_900 Class'] = 1
df_num.loc[ (df_num.國小_800_900>=2) & (df_num.國小_800_900<=3), '國小_800_900 Class'] = 2
df_num.loc[ (df_num.國小_800_900>=4) & (df_num.國小_800_900<=6), '國小_800_900 Class'] = 3

df_num.loc[ (df_num.國小_900_1000>=0) & (df_num.國小_900_1000<=1), '國小_900_1000 Class'] = 1
df_num.loc[ (df_num.國小_900_1000>=2) & (df_num.國小_900_1000<=3), '國小_900_1000 Class'] = 2
df_num.loc[ (df_num.國小_900_1000>=4) & (df_num.國小_900_1000<=6), '國小_900_1000 Class'] = 3

# 將國中做分組
df_num.loc[ (df_num.國中_0_100>=0) & (df_num.國中_0_100<=1), '國中_0_100 Class'] = 1
df_num.loc[ (df_num.國中_0_100>=2) & (df_num.國中_0_100<=3), '國中_0_100 Class'] = 2
df_num.loc[ (df_num.國中_0_100>=4) & (df_num.國中_0_100<=7), '國中_0_100 Class'] = 3

df_num.loc[ (df_num.國中_100_200>=0) & (df_num.國中_100_200<=1), '國中_100_200 Class'] = 1
df_num.loc[ (df_num.國中_100_200>=2) & (df_num.國中_100_200<=3), '國中_100_200 Class'] = 2
df_num.loc[ (df_num.國中_100_200>=4) & (df_num.國中_100_200<=7), '國中_100_200 Class'] = 3

df_num.loc[ (df_num.國中_200_300>=0) & (df_num.國中_200_300<=1), '國中_200_300 Class'] = 1
df_num.loc[ (df_num.國中_200_300>=2) & (df_num.國中_200_300<=3), '國中_200_300 Class'] = 2
df_num.loc[ (df_num.國中_200_300>=4) & (df_num.國中_200_300<=7), '國中_200_300 Class'] = 3

df_num.loc[ (df_num.國中_300_400>=0) & (df_num.國中_300_400<=1), '國中_300_400 Class'] = 1
df_num.loc[ (df_num.國中_300_400>=2) & (df_num.國中_300_400<=3), '國中_300_400 Class'] = 2
df_num.loc[ (df_num.國中_300_400>=4) & (df_num.國中_300_400<=7), '國中_300_400 Class'] = 3

df_num.loc[ (df_num.國中_400_500>=0) & (df_num.國中_400_500<=1), '國中_400_500 Class'] = 1
df_num.loc[ (df_num.國中_400_500>=2) & (df_num.國中_400_500<=3), '國中_400_500 Class'] = 2
df_num.loc[ (df_num.國中_400_500>=4) & (df_num.國中_400_500<=7), '國中_400_500 Class'] = 3

df_num.loc[ (df_num.國中_500_600>=0) & (df_num.國中_500_600<=1), '國中_500_600 Class'] = 1
df_num.loc[ (df_num.國中_500_600>=2) & (df_num.國中_500_600<=3), '國中_500_600 Class'] = 2
df_num.loc[ (df_num.國中_500_600>=4) & (df_num.國中_500_600<=7), '國中_500_600 Class'] = 3

df_num.loc[ (df_num.國中_600_700>=0) & (df_num.國中_600_700<=1), '國中_600_700 Class'] = 1
df_num.loc[ (df_num.國中_600_700>=2) & (df_num.國中_600_700<=3), '國中_600_700 Class'] = 2
df_num.loc[ (df_num.國中_600_700>=4) & (df_num.國中_600_700<=7), '國中_600_700 Class'] = 3

df_num.loc[ (df_num.國中_700_800>=0) & (df_num.國中_700_800<=1), '國中_700_800 Class'] = 1
df_num.loc[ (df_num.國中_700_800>=2) & (df_num.國中_700_800<=3), '國中_700_800 Class'] = 2
df_num.loc[ (df_num.國中_700_800>=4) & (df_num.國中_700_800<=7), '國中_700_800 Class'] = 3

df_num.loc[ (df_num.國中_800_900>=0) & (df_num.國中_800_900<=1), '國中_800_900 Class'] = 1
df_num.loc[ (df_num.國中_800_900>=2) & (df_num.國中_800_900<=3), '國中_800_900 Class'] = 2
df_num.loc[ (df_num.國中_800_900>=4) & (df_num.國中_800_900<=7), '國中_800_900 Class'] = 3

df_num.loc[ (df_num.國中_900_1000>=0) & (df_num.國中_900_1000<=1), '國中_900_1000 Class'] = 1
df_num.loc[ (df_num.國中_900_1000>=2) & (df_num.國中_900_1000<=3), '國中_900_1000 Class'] = 2
df_num.loc[ (df_num.國中_900_1000>=4) & (df_num.國中_900_1000<=7), '國中_900_1000 Class'] = 3

# 將高中做分組
df_num.loc[ (df_num.高中_0_100>=0) & (df_num.高中_0_100<=2), '高中_0_100 Class'] = 1
df_num.loc[ (df_num.高中_0_100>=3) & (df_num.高中_0_100<=6), '高中_0_100 Class'] = 2
df_num.loc[ (df_num.高中_0_100>=7) & (df_num.高中_0_100<=9), '高中_0_100 Class'] = 3

df_num.loc[ (df_num.高中_100_200>=0) & (df_num.高中_100_200<=2), '高中_100_200 Class'] = 1
df_num.loc[ (df_num.高中_100_200>=3) & (df_num.高中_100_200<=6), '高中_100_200 Class'] = 2
df_num.loc[ (df_num.高中_100_200>=7) & (df_num.高中_100_200<=9), '高中_100_200 Class'] = 3

df_num.loc[ (df_num.高中_200_300>=0) & (df_num.高中_200_300<=2), '高中_200_300 Class'] = 1
df_num.loc[ (df_num.高中_200_300>=3) & (df_num.高中_200_300<=6), '高中_200_300 Class'] = 2
df_num.loc[ (df_num.高中_200_300>=7) & (df_num.高中_200_300<=9), '高中_200_300 Class'] = 3

df_num.loc[ (df_num.高中_300_400>=0) & (df_num.高中_300_400<=2), '高中_300_400 Class'] = 1
df_num.loc[ (df_num.高中_300_400>=3) & (df_num.高中_300_400<=6), '高中_300_400 Class'] = 2
df_num.loc[ (df_num.高中_300_400>=7) & (df_num.高中_300_400<=9), '高中_300_400 Class'] = 3

df_num.loc[ (df_num.高中_400_500>=0) & (df_num.高中_400_500<=2), '高中_400_500 Class'] = 1
df_num.loc[ (df_num.高中_400_500>=3) & (df_num.高中_400_500<=6), '高中_400_500 Class'] = 2
df_num.loc[ (df_num.高中_400_500>=7) & (df_num.高中_400_500<=9), '高中_400_500 Class'] = 3

df_num.loc[ (df_num.高中_500_600>=0) & (df_num.高中_500_600<=2), '高中_500_600 Class'] = 1
df_num.loc[ (df_num.高中_500_600>=3) & (df_num.高中_500_600<=6), '高中_500_600 Class'] = 2
df_num.loc[ (df_num.高中_500_600>=7) & (df_num.高中_500_600<=9), '高中_500_600 Class'] = 3

df_num.loc[ (df_num.高中_600_700>=0) & (df_num.高中_600_700<=2), '高中_600_700 Class'] = 1
df_num.loc[ (df_num.高中_600_700>=3) & (df_num.高中_600_700<=6), '高中_600_700 Class'] = 2
df_num.loc[ (df_num.高中_600_700>=7) & (df_num.高中_600_700<=9), '高中_600_700 Class'] = 3

df_num.loc[ (df_num.高中_700_800>=0) & (df_num.高中_700_800<=2), '高中_700_800 Class'] = 1
df_num.loc[ (df_num.高中_700_800>=3) & (df_num.高中_700_800<=6), '高中_700_800 Class'] = 2
df_num.loc[ (df_num.高中_700_800>=7) & (df_num.高中_700_800<=9), '高中_700_800 Class'] = 3

df_num.loc[ (df_num.高中_800_900>=0) & (df_num.高中_800_900<=2), '高中_800_900 Class'] = 1
df_num.loc[ (df_num.高中_800_900>=3) & (df_num.高中_800_900<=6), '高中_800_900 Class'] = 2
df_num.loc[ (df_num.高中_800_900>=7) & (df_num.高中_800_900<=9), '高中_800_900 Class'] = 3

df_num.loc[ (df_num.高中_900_1000>=0) & (df_num.高中_900_1000<=2), '高中_900_1000 Class'] = 1
df_num.loc[ (df_num.高中_900_1000>=3) & (df_num.高中_900_1000<=6), '高中_900_1000 Class'] = 2
df_num.loc[ (df_num.高中_900_1000>=7) & (df_num.高中_900_1000<=9), '高中_900_1000 Class'] = 3

# 將高職做分組
df_num.loc[ (df_num.高職_0_100>=0) & (df_num.高職_0_100<=1), '高職_0_100 Class'] = 1
df_num.loc[ (df_num.高職_0_100>=2) & (df_num.高職_0_100<=3), '高職_0_100 Class'] = 2
df_num.loc[ (df_num.高職_0_100>=4) & (df_num.高職_0_100<=5), '高職_0_100 Class'] = 3

df_num.loc[ (df_num.高職_100_200>=0) & (df_num.高職_100_200<=1), '高職_100_200 Class'] = 1
df_num.loc[ (df_num.高職_100_200>=2) & (df_num.高職_100_200<=3), '高職_100_200 Class'] = 2
df_num.loc[ (df_num.高職_100_200>=4) & (df_num.高職_100_200<=5), '高職_100_200 Class'] = 3

df_num.loc[ (df_num.高職_200_300>=0) & (df_num.高職_200_300<=1), '高職_200_300 Class'] = 1
df_num.loc[ (df_num.高職_200_300>=2) & (df_num.高職_200_300<=3), '高職_200_300 Class'] = 2
df_num.loc[ (df_num.高職_200_300>=4) & (df_num.高職_200_300<=5), '高職_200_300 Class'] = 3

df_num.loc[ (df_num.高職_300_400>=0) & (df_num.高職_300_400<=1), '高職_300_400 Class'] = 1
df_num.loc[ (df_num.高職_300_400>=2) & (df_num.高職_300_400<=3), '高職_300_400 Class'] = 2
df_num.loc[ (df_num.高職_300_400>=4) & (df_num.高職_300_400<=5), '高職_300_400 Class'] = 3

df_num.loc[ (df_num.高職_400_500>=0) & (df_num.高職_400_500<=1), '高職_400_500 Class'] = 1
df_num.loc[ (df_num.高職_400_500>=2) & (df_num.高職_400_500<=3), '高職_400_500 Class'] = 2
df_num.loc[ (df_num.高職_400_500>=4) & (df_num.高職_400_500<=5), '高職_400_500 Class'] = 3

df_num.loc[ (df_num.高職_500_600>=0) & (df_num.高職_500_600<=1), '高職_500_600 Class'] = 1
df_num.loc[ (df_num.高職_500_600>=2) & (df_num.高職_500_600<=3), '高職_500_600 Class'] = 2
df_num.loc[ (df_num.高職_500_600>=4) & (df_num.高職_500_600<=5), '高職_500_600 Class'] = 3

df_num.loc[ (df_num.高職_600_700>=0) & (df_num.高職_600_700<=1), '高職_600_700 Class'] = 1
df_num.loc[ (df_num.高職_600_700>=2) & (df_num.高職_600_700<=3), '高職_600_700 Class'] = 2
df_num.loc[ (df_num.高職_600_700>=4) & (df_num.高職_600_700<=5), '高職_600_700 Class'] = 3

df_num.loc[ (df_num.高職_700_800>=0) & (df_num.高職_700_800<=1), '高職_700_800 Class'] = 1
df_num.loc[ (df_num.高職_700_800>=2) & (df_num.高職_700_800<=3), '高職_700_800 Class'] = 2
df_num.loc[ (df_num.高職_700_800>=4) & (df_num.高職_700_800<=5), '高職_700_800 Class'] = 3

df_num.loc[ (df_num.高職_800_900>=0) & (df_num.高職_800_900<=1), '高職_800_900 Class'] = 1
df_num.loc[ (df_num.高職_800_900>=2) & (df_num.高職_800_900<=3), '高職_800_900 Class'] = 2
df_num.loc[ (df_num.高職_800_900>=4) & (df_num.高職_800_900<=5), '高職_800_900 Class'] = 3

df_num.loc[ (df_num.高職_900_1000>=0) & (df_num.高職_900_1000<=1), '高職_900_1000 Class'] = 1
df_num.loc[ (df_num.高職_900_1000>=2) & (df_num.高職_900_1000<=3), '高職_900_1000 Class'] = 2
df_num.loc[ (df_num.高職_900_1000>=4) & (df_num.高職_900_1000<=5), '高職_900_1000 Class'] = 3

# 將大學做分組
df_num.loc[ (df_num.大學_0_100>=0) & (df_num.大學_0_100<=1), '大學_0_100 Class'] = 1
df_num.loc[ (df_num.大學_0_100>=2) & (df_num.大學_0_100<=3), '大學_0_100 Class'] = 2
df_num.loc[ (df_num.大學_0_100>=4) & (df_num.大學_0_100<=13), '大學_0_100 Class'] = 3

df_num.loc[ (df_num.大學_100_200>=0) & (df_num.大學_100_200<=1), '大學_100_200 Class'] = 1
df_num.loc[ (df_num.大學_100_200>=2) & (df_num.大學_100_200<=3), '大學_100_200 Class'] = 2
df_num.loc[ (df_num.大學_100_200>=4) & (df_num.大學_100_200<=13), '大學_100_200 Class'] = 3

df_num.loc[ (df_num.大學_200_300>=0) & (df_num.大學_200_300<=1), '大學_200_300 Class'] = 1
df_num.loc[ (df_num.大學_200_300>=2) & (df_num.大學_200_300<=3), '大學_200_300 Class'] = 2
df_num.loc[ (df_num.大學_200_300>=4) & (df_num.大學_200_300<=13), '大學_200_300 Class'] = 3

df_num.loc[ (df_num.大學_300_400>=0) & (df_num.大學_300_400<=1), '大學_300_400 Class'] = 1
df_num.loc[ (df_num.大學_300_400>=2) & (df_num.大學_300_400<=3), '大學_300_400 Class'] = 2
df_num.loc[ (df_num.大學_300_400>=4) & (df_num.大學_300_400<=13), '大學_300_400 Class'] = 3

df_num.loc[ (df_num.大學_400_500>=0) & (df_num.大學_400_500<=1), '大學_400_500 Class'] = 1
df_num.loc[ (df_num.大學_400_500>=2) & (df_num.大學_400_500<=3), '大學_400_500 Class'] = 2
df_num.loc[ (df_num.大學_400_500>=4) & (df_num.大學_400_500<=13), '大學_400_500 Class'] = 3

df_num.loc[ (df_num.大學_500_600>=0) & (df_num.大學_500_600<=1), '大學_500_600 Class'] = 1
df_num.loc[ (df_num.大學_500_600>=2) & (df_num.大學_500_600<=3), '大學_500_600 Class'] = 2
df_num.loc[ (df_num.大學_500_600>=4) & (df_num.大學_500_600<=13), '大學_500_600 Class'] = 3

df_num.loc[ (df_num.大學_600_700>=0) & (df_num.大學_600_700<=1), '大學_600_700 Class'] = 1
df_num.loc[ (df_num.大學_600_700>=2) & (df_num.大學_600_700<=3), '大學_600_700 Class'] = 2
df_num.loc[ (df_num.大學_600_700>=4) & (df_num.大學_600_700<=13), '大學_600_700 Class'] = 3

df_num.loc[ (df_num.大學_700_800>=0) & (df_num.大學_700_800<=1), '大學_700_800 Class'] = 1
df_num.loc[ (df_num.大學_700_800>=2) & (df_num.大學_700_800<=3), '大學_700_800 Class'] = 2
df_num.loc[ (df_num.大學_700_800>=4) & (df_num.大學_700_800<=13), '大學_700_800 Class'] = 3

df_num.loc[ (df_num.大學_800_900>=0) & (df_num.大學_800_900<=1), '大學_800_900 Class'] = 1
df_num.loc[ (df_num.大學_800_900>=2) & (df_num.大學_800_900<=3), '大學_800_900 Class'] = 2
df_num.loc[ (df_num.大學_800_900>=4) & (df_num.大學_800_900<=13), '大學_800_900 Class'] = 3

df_num.loc[ (df_num.大學_900_1000>=0) & (df_num.大學_900_1000<=1), '大學_900_1000 Class'] = 1
df_num.loc[ (df_num.大學_900_1000>=2) & (df_num.大學_900_1000<=3), '大學_900_1000 Class'] = 2
df_num.loc[ (df_num.大學_900_1000>=4) & (df_num.大學_900_1000<=13), '大學_900_1000 Class'] = 3

# 將科大做分組
df_num.loc[ (df_num.科大_0_100>=0) & (df_num.科大_0_100<=1), '科大_0_100 Class'] = 1
df_num.loc[ (df_num.科大_0_100>=2) & (df_num.科大_0_100<=3), '科大_0_100 Class'] = 2
df_num.loc[ (df_num.科大_0_100>=4) & (df_num.科大_0_100<=14), '科大_0_100 Class'] = 3

df_num.loc[ (df_num.科大_100_200>=0) & (df_num.科大_100_200<=1), '科大_100_200 Class'] = 1
df_num.loc[ (df_num.科大_100_200>=2) & (df_num.科大_100_200<=3), '科大_100_200 Class'] = 2
df_num.loc[ (df_num.科大_100_200>=4) & (df_num.科大_100_200<=14), '科大_100_200 Class'] = 3

df_num.loc[ (df_num.科大_200_300>=0) & (df_num.科大_200_300<=1), '科大_200_300 Class'] = 1
df_num.loc[ (df_num.科大_200_300>=2) & (df_num.科大_200_300<=3), '科大_200_300 Class'] = 2
df_num.loc[ (df_num.科大_200_300>=4) & (df_num.科大_200_300<=14), '科大_200_300 Class'] = 3

df_num.loc[ (df_num.科大_300_400>=0) & (df_num.科大_300_400<=1), '科大_300_400 Class'] = 1
df_num.loc[ (df_num.科大_300_400>=2) & (df_num.科大_300_400<=3), '科大_300_400 Class'] = 2
df_num.loc[ (df_num.科大_300_400>=4) & (df_num.科大_300_400<=14), '科大_300_400 Class'] = 3

df_num.loc[ (df_num.科大_400_500>=0) & (df_num.科大_400_500<=1), '科大_400_500 Class'] = 1
df_num.loc[ (df_num.科大_400_500>=2) & (df_num.科大_400_500<=3), '科大_400_500 Class'] = 2
df_num.loc[ (df_num.科大_400_500>=4) & (df_num.科大_400_500<=14), '科大_400_500 Class'] = 3

df_num.loc[ (df_num.科大_500_600>=0) & (df_num.科大_500_600<=1), '科大_500_600 Class'] = 1
df_num.loc[ (df_num.科大_500_600>=2) & (df_num.科大_500_600<=3), '科大_500_600 Class'] = 2
df_num.loc[ (df_num.科大_500_600>=4) & (df_num.科大_500_600<=14), '科大_500_600 Class'] = 3

df_num.loc[ (df_num.科大_600_700>=0) & (df_num.科大_600_700<=1), '科大_600_700 Class'] = 1
df_num.loc[ (df_num.科大_600_700>=2) & (df_num.科大_600_700<=3), '科大_600_700 Class'] = 2
df_num.loc[ (df_num.科大_600_700>=4) & (df_num.科大_600_700<=14), '科大_600_700 Class'] = 3

df_num.loc[ (df_num.科大_700_800>=0) & (df_num.科大_700_800<=1), '科大_700_800 Class'] = 1
df_num.loc[ (df_num.科大_700_800>=2) & (df_num.科大_700_800<=3), '科大_700_800 Class'] = 2
df_num.loc[ (df_num.科大_700_800>=4) & (df_num.科大_700_800<=14), '科大_700_800 Class'] = 3

df_num.loc[ (df_num.科大_800_900>=0) & (df_num.科大_800_900<=1), '科大_800_900 Class'] = 1
df_num.loc[ (df_num.科大_800_900>=2) & (df_num.科大_800_900<=3), '科大_800_900 Class'] = 2
df_num.loc[ (df_num.科大_800_900>=4) & (df_num.科大_800_900<=14), '科大_800_900 Class'] = 3

df_num.loc[ (df_num.科大_900_1000>=0) & (df_num.科大_900_1000<=1), '科大_900_1000 Class'] = 1
df_num.loc[ (df_num.科大_900_1000>=2) & (df_num.科大_900_1000<=3), '科大_900_1000 Class'] = 2
df_num.loc[ (df_num.科大_900_1000>=4) & (df_num.科大_900_1000<=14), '科大_900_1000 Class'] = 3

# 將學校做分組
df_num.loc[ (df_num.學校_0_100>=0) & (df_num.學校_0_100<=4), '學校_0_100 Class'] = 1
df_num.loc[ (df_num.學校_0_100>=5) & (df_num.學校_0_100<=7), '學校_0_100 Class'] = 2
df_num.loc[ (df_num.學校_0_100>=8) & (df_num.學校_0_100<=11), '學校_0_100 Class'] = 3

df_num.loc[ (df_num.學校_100_200>=0) & (df_num.學校_100_200<=4), '學校_100_200 Class'] = 1
df_num.loc[ (df_num.學校_100_200>=5) & (df_num.學校_100_200<=7), '學校_100_200 Class'] = 2
df_num.loc[ (df_num.學校_100_200>=8) & (df_num.學校_100_200<=11), '學校_100_200 Class'] = 3

df_num.loc[ (df_num.學校_200_300>=0) & (df_num.學校_200_300<=4), '學校_200_300 Class'] = 1
df_num.loc[ (df_num.學校_200_300>=5) & (df_num.學校_200_300<=7), '學校_200_300 Class'] = 2
df_num.loc[ (df_num.學校_200_300>=8) & (df_num.學校_200_300<=11), '學校_200_300 Class'] = 3

df_num.loc[ (df_num.學校_300_400>=0) & (df_num.學校_300_400<=4), '學校_300_400 Class'] = 1
df_num.loc[ (df_num.學校_300_400>=5) & (df_num.學校_300_400<=7), '學校_300_400 Class'] = 2
df_num.loc[ (df_num.學校_300_400>=8) & (df_num.學校_300_400<=11), '學校_300_400 Class'] = 3

df_num.loc[ (df_num.學校_400_500>=0) & (df_num.學校_400_500<=4), '學校_400_500 Class'] = 1
df_num.loc[ (df_num.學校_400_500>=5) & (df_num.學校_400_500<=7), '學校_400_500 Class'] = 2
df_num.loc[ (df_num.學校_400_500>=8) & (df_num.學校_400_500<=11), '學校_400_500 Class'] = 3

df_num.loc[ (df_num.學校_500_600>=0) & (df_num.學校_500_600<=4), '學校_500_600 Class'] = 1
df_num.loc[ (df_num.學校_500_600>=5) & (df_num.學校_500_600<=7), '學校_500_600 Class'] = 2
df_num.loc[ (df_num.學校_500_600>=8) & (df_num.學校_500_600<=11), '學校_500_600 Class'] = 3

df_num.loc[ (df_num.學校_600_700>=0) & (df_num.學校_600_700<=4), '學校_600_700 Class'] = 1
df_num.loc[ (df_num.學校_600_700>=5) & (df_num.學校_600_700<=7), '學校_600_700 Class'] = 2
df_num.loc[ (df_num.學校_600_700>=8) & (df_num.學校_600_700<=11), '學校_600_700 Class'] = 3

df_num.loc[ (df_num.學校_700_800>=0) & (df_num.學校_700_800<=4), '學校_700_800 Class'] = 1
df_num.loc[ (df_num.學校_700_800>=5) & (df_num.學校_700_800<=7), '學校_700_800 Class'] = 2
df_num.loc[ (df_num.學校_700_800>=8) & (df_num.學校_700_800<=11), '學校_700_800 Class'] = 3

df_num.loc[ (df_num.學校_800_900>=0) & (df_num.學校_800_900<=4), '學校_800_900 Class'] = 1
df_num.loc[ (df_num.學校_800_900>=5) & (df_num.學校_800_900<=7), '學校_800_900 Class'] = 2
df_num.loc[ (df_num.學校_800_900>=8) & (df_num.學校_800_900<=11), '學校_800_900 Class'] = 3

df_num.loc[ (df_num.學校_900_1000>=0) & (df_num.學校_900_1000<=4), '學校_900_1000 Class'] = 1
df_num.loc[ (df_num.學校_900_1000>=5) & (df_num.學校_900_1000<=7), '學校_900_1000 Class'] = 2
df_num.loc[ (df_num.學校_900_1000>=8) & (df_num.學校_900_1000<=11), '學校_900_1000 Class'] = 3

# 將商圈做分組
df_num.loc[ (df_num.商圈_0_100>=0) & (df_num.商圈_0_100<=4), '商圈_0_100 Class'] = 1
df_num.loc[ (df_num.商圈_0_100>=5) & (df_num.商圈_0_100<=7), '商圈_0_100 Class'] = 2
df_num.loc[ (df_num.商圈_0_100>=8) & (df_num.商圈_0_100<=10), '商圈_0_100 Class'] = 3

df_num.loc[ (df_num.商圈_100_200>=0) & (df_num.商圈_100_200<=4), '商圈_100_200 Class'] = 1
df_num.loc[ (df_num.商圈_100_200>=5) & (df_num.商圈_100_200<=7), '商圈_100_200 Class'] = 2
df_num.loc[ (df_num.商圈_100_200>=8) & (df_num.商圈_100_200<=10), '商圈_100_200 Class'] = 3

df_num.loc[ (df_num.商圈_200_300>=0) & (df_num.商圈_200_300<=4), '商圈_200_300 Class'] = 1
df_num.loc[ (df_num.商圈_200_300>=5) & (df_num.商圈_200_300<=7), '商圈_200_300 Class'] = 2
df_num.loc[ (df_num.商圈_200_300>=8) & (df_num.商圈_200_300<=10), '商圈_200_300 Class'] = 3

df_num.loc[ (df_num.商圈_300_400>=0) & (df_num.商圈_300_400<=4), '商圈_300_400 Class'] = 1
df_num.loc[ (df_num.商圈_300_400>=5) & (df_num.商圈_300_400<=7), '商圈_300_400 Class'] = 2
df_num.loc[ (df_num.商圈_300_400>=8) & (df_num.商圈_300_400<=10), '商圈_300_400 Class'] = 3

df_num.loc[ (df_num.商圈_400_500>=0) & (df_num.商圈_400_500<=4), '商圈_400_500 Class'] = 1
df_num.loc[ (df_num.商圈_400_500>=5) & (df_num.商圈_400_500<=7), '商圈_400_500 Class'] = 2
df_num.loc[ (df_num.商圈_400_500>=8) & (df_num.商圈_400_500<=10), '商圈_400_500 Class'] = 3

df_num.loc[ (df_num.商圈_500_600>=0) & (df_num.商圈_500_600<=4), '商圈_500_600 Class'] = 1
df_num.loc[ (df_num.商圈_500_600>=5) & (df_num.商圈_500_600<=7), '商圈_500_600 Class'] = 2
df_num.loc[ (df_num.商圈_500_600>=8) & (df_num.商圈_500_600<=10), '商圈_500_600 Class'] = 3

df_num.loc[ (df_num.商圈_600_700>=0) & (df_num.商圈_600_700<=4), '商圈_600_700 Class'] = 1
df_num.loc[ (df_num.商圈_600_700>=5) & (df_num.商圈_600_700<=7), '商圈_600_700 Class'] = 2
df_num.loc[ (df_num.商圈_600_700>=8) & (df_num.商圈_600_700<=10), '商圈_600_700 Class'] = 3

df_num.loc[ (df_num.商圈_700_800>=0) & (df_num.商圈_700_800<=4), '商圈_700_800 Class'] = 1
df_num.loc[ (df_num.商圈_700_800>=5) & (df_num.商圈_700_800<=7), '商圈_700_800 Class'] = 2
df_num.loc[ (df_num.商圈_700_800>=8) & (df_num.商圈_700_800<=10), '商圈_700_800 Class'] = 3

df_num.loc[ (df_num.商圈_800_900>=0) & (df_num.商圈_800_900<=4), '商圈_800_900 Class'] = 1
df_num.loc[ (df_num.商圈_800_900>=5) & (df_num.商圈_800_900<=7), '商圈_800_900 Class'] = 2
df_num.loc[ (df_num.商圈_800_900>=8) & (df_num.商圈_800_900<=10), '商圈_800_900 Class'] = 3

df_num.loc[ (df_num.商圈_900_1000>=0) & (df_num.商圈_900_1000<=4), '商圈_900_1000 Class'] = 1
df_num.loc[ (df_num.商圈_900_1000>=5) & (df_num.商圈_900_1000<=7), '商圈_900_1000 Class'] = 2
df_num.loc[ (df_num.商圈_900_1000>=8) & (df_num.商圈_900_1000<=10), '商圈_900_1000 Class'] = 3

# 將星巴克做分組
df_num.loc[ (df_num.星巴克_0_100>=0) & (df_num.星巴克_0_100<=1), '星巴克_0_100 Class'] = 1
df_num.loc[ (df_num.星巴克_0_100==2), '星巴克_0_100 Class'] = 2
df_num.loc[ (df_num.星巴克_0_100>=3) & (df_num.星巴克_0_100<=4), '星巴克_0_100 Class'] = 3

df_num.loc[ (df_num.星巴克_100_200>=0) & (df_num.星巴克_100_200<=1), '星巴克_100_200 Class'] = 1
df_num.loc[ (df_num.星巴克_100_200==2), '星巴克_100_200 Class'] = 2
df_num.loc[ (df_num.星巴克_100_200>=3) & (df_num.星巴克_100_200<=4), '星巴克_100_200 Class'] = 3

df_num.loc[ (df_num.星巴克_200_300>=0) & (df_num.星巴克_200_300<=1), '星巴克_200_300 Class'] = 1
df_num.loc[ (df_num.星巴克_200_300==2), '星巴克_200_300 Class'] = 2
df_num.loc[ (df_num.星巴克_200_300>=3) & (df_num.星巴克_200_300<=4), '星巴克_200_300 Class'] = 3

df_num.loc[ (df_num.星巴克_300_400>=0) & (df_num.星巴克_300_400<=1), '星巴克_300_400 Class'] = 1
df_num.loc[ (df_num.星巴克_300_400==2), '星巴克_300_400 Class'] = 2
df_num.loc[ (df_num.星巴克_300_400>=3) & (df_num.星巴克_300_400<=4), '星巴克_300_400 Class'] = 3

df_num.loc[ (df_num.星巴克_400_500>=0) & (df_num.星巴克_400_500<=1), '星巴克_400_500 Class'] = 1
df_num.loc[ (df_num.星巴克_400_500==2), '星巴克_400_500 Class'] = 2
df_num.loc[ (df_num.星巴克_400_500>=3) & (df_num.星巴克_400_500<=4), '星巴克_400_500 Class'] = 3

df_num.loc[ (df_num.星巴克_500_600>=0) & (df_num.星巴克_500_600<=1), '星巴克_500_600 Class'] = 1
df_num.loc[ (df_num.星巴克_500_600==2), '星巴克_500_600 Class'] = 2
df_num.loc[ (df_num.星巴克_500_600>=3) & (df_num.星巴克_500_600<=4), '星巴克_500_600 Class'] = 3

df_num.loc[ (df_num.星巴克_600_700>=0) & (df_num.星巴克_600_700<=1), '星巴克_600_700 Class'] = 1
df_num.loc[ (df_num.星巴克_600_700==2), '星巴克_600_700 Class'] = 2
df_num.loc[ (df_num.星巴克_600_700>=3) & (df_num.星巴克_600_700<=4), '星巴克_600_700 Class'] = 3

df_num.loc[ (df_num.星巴克_700_800>=0) & (df_num.星巴克_700_800<=1), '星巴克_700_800 Class'] = 1
df_num.loc[ (df_num.星巴克_700_800==2), '星巴克_700_800 Class'] = 2
df_num.loc[ (df_num.星巴克_700_800>=3) & (df_num.星巴克_700_800<=4), '星巴克_700_800 Class'] = 3

df_num.loc[ (df_num.星巴克_800_900>=0) & (df_num.星巴克_800_900<=1), '星巴克_800_900 Class'] = 1
df_num.loc[ (df_num.星巴克_800_900==2), '星巴克_800_900 Class'] = 2
df_num.loc[ (df_num.星巴克_800_900>=3) & (df_num.星巴克_800_900<=4), '星巴克_800_900 Class'] = 3

df_num.loc[ (df_num.星巴克_900_1000>=0) & (df_num.星巴克_900_1000<=1), '星巴克_900_1000 Class'] = 1
df_num.loc[ (df_num.星巴克_900_1000==2), '星巴克_900_1000 Class'] = 2
df_num.loc[ (df_num.星巴克_900_1000>=3) & (df_num.星巴克_900_1000<=4), '星巴克_900_1000 Class'] = 3

# 將大潤發作分組
df_num.loc[ (df_num.大潤發_0_100>=0) & (df_num.大潤發_0_100<=5), '大潤發_0_100 Class'] = 1
df_num.loc[ (df_num.大潤發_0_100>=6) & (df_num.大潤發_0_100<=10), '大潤發_0_100 Class'] = 2
df_num.loc[ (df_num.大潤發_0_100>=11) & (df_num.大潤發_0_100<=20), '大潤發_0_100 Class'] = 3

df_num.loc[ (df_num.大潤發_100_200>=0) & (df_num.大潤發_100_200<=5), '大潤發_100_200 Class'] = 1
df_num.loc[ (df_num.大潤發_100_200>=6) & (df_num.大潤發_100_200<=10), '大潤發_100_200 Class'] = 2
df_num.loc[ (df_num.大潤發_100_200>=11) & (df_num.大潤發_100_200<=20), '大潤發_100_200 Class'] = 3

df_num.loc[ (df_num.大潤發_200_300>=0) & (df_num.大潤發_200_300<=5), '大潤發_200_300 Class'] = 1
df_num.loc[ (df_num.大潤發_200_300>=6) & (df_num.大潤發_200_300<=10), '大潤發_200_300 Class'] = 2
df_num.loc[ (df_num.大潤發_200_300>=11) & (df_num.大潤發_200_300<=20), '大潤發_200_300 Class'] = 3

df_num.loc[ (df_num.大潤發_300_400>=0) & (df_num.大潤發_300_400<=5), '大潤發_300_400 Class'] = 1
df_num.loc[ (df_num.大潤發_300_400>=6) & (df_num.大潤發_300_400<=10), '大潤發_300_400 Class'] = 2
df_num.loc[ (df_num.大潤發_300_400>=11) & (df_num.大潤發_300_400<=20), '大潤發_300_400 Class'] = 3

df_num.loc[ (df_num.大潤發_400_500>=0) & (df_num.大潤發_400_500<=5), '大潤發_400_500 Class'] = 1
df_num.loc[ (df_num.大潤發_400_500>=6) & (df_num.大潤發_400_500<=10), '大潤發_400_500 Class'] = 2
df_num.loc[ (df_num.大潤發_400_500>=11) & (df_num.大潤發_400_500<=20), '大潤發_400_500 Class'] = 3

df_num.loc[ (df_num.大潤發_500_600>=0) & (df_num.大潤發_500_600<=5), '大潤發_500_600 Class'] = 1
df_num.loc[ (df_num.大潤發_500_600>=6) & (df_num.大潤發_500_600<=10), '大潤發_500_600 Class'] = 2
df_num.loc[ (df_num.大潤發_500_600>=11) & (df_num.大潤發_500_600<=20), '大潤發_500_600 Class'] = 3

df_num.loc[ (df_num.大潤發_600_700>=0) & (df_num.大潤發_600_700<=5), '大潤發_600_700 Class'] = 1
df_num.loc[ (df_num.大潤發_600_700>=6) & (df_num.大潤發_600_700<=10), '大潤發_600_700 Class'] = 2
df_num.loc[ (df_num.大潤發_600_700>=11) & (df_num.大潤發_600_700<=20), '大潤發_600_700 Class'] = 3

df_num.loc[ (df_num.大潤發_700_800>=0) & (df_num.大潤發_700_800<=5), '大潤發_700_800 Class'] = 1
df_num.loc[ (df_num.大潤發_700_800>=6) & (df_num.大潤發_700_800<=10), '大潤發_700_800 Class'] = 2
df_num.loc[ (df_num.大潤發_700_800>=11) & (df_num.大潤發_700_800<=20), '大潤發_700_800 Class'] = 3

df_num.loc[ (df_num.大潤發_800_900>=0) & (df_num.大潤發_800_900<=5), '大潤發_800_900 Class'] = 1
df_num.loc[ (df_num.大潤發_800_900>=6) & (df_num.大潤發_800_900<=10), '大潤發_800_900 Class'] = 2
df_num.loc[ (df_num.大潤發_800_900>=11) & (df_num.大潤發_800_900<=20), '大潤發_800_900 Class'] = 3

df_num.loc[ (df_num.大潤發_900_1000>=0) & (df_num.大潤發_900_1000<=5), '大潤發_900_1000 Class'] = 1
df_num.loc[ (df_num.大潤發_900_1000>=6) & (df_num.大潤發_900_1000<=10), '大潤發_900_1000 Class'] = 2
df_num.loc[ (df_num.大潤發_900_1000>=11) & (df_num.大潤發_900_1000<=20), '大潤發_900_1000 Class'] = 3

# 將家樂福做分組
df_num.loc[ (df_num.家樂福_0_100>=0) & (df_num.家樂福_0_100<=2), '家樂福_0_100 Class'] = 1
df_num.loc[ (df_num.家樂福_0_100>=3) & (df_num.家樂福_0_100<=7), '家樂福_0_100 Class'] = 2
df_num.loc[ (df_num.家樂福_0_100>=8) & (df_num.家樂福_0_100<=14), '家樂福_0_100 Class'] = 3

df_num.loc[ (df_num.家樂福_100_200>=0) & (df_num.家樂福_100_200<=2), '家樂福_100_200 Class'] = 1
df_num.loc[ (df_num.家樂福_100_200>=3) & (df_num.家樂福_100_200<=7), '家樂福_100_200 Class'] = 2
df_num.loc[ (df_num.家樂福_100_200>=8) & (df_num.家樂福_100_200<=14), '家樂福_100_200 Class'] = 3

df_num.loc[ (df_num.家樂福_200_300>=0) & (df_num.家樂福_200_300<=2), '家樂福_200_300 Class'] = 1
df_num.loc[ (df_num.家樂福_200_300>=3) & (df_num.家樂福_200_300<=7), '家樂福_200_300 Class'] = 2
df_num.loc[ (df_num.家樂福_200_300>=8) & (df_num.家樂福_200_300<=14), '家樂福_200_300 Class'] = 3

df_num.loc[ (df_num.家樂福_300_400>=0) & (df_num.家樂福_300_400<=2), '家樂福_300_400 Class'] = 1
df_num.loc[ (df_num.家樂福_300_400>=3) & (df_num.家樂福_300_400<=7), '家樂福_300_400 Class'] = 2
df_num.loc[ (df_num.家樂福_300_400>=8) & (df_num.家樂福_300_400<=14), '家樂福_300_400 Class'] = 3

df_num.loc[ (df_num.家樂福_400_500>=0) & (df_num.家樂福_400_500<=2), '家樂福_400_500 Class'] = 1
df_num.loc[ (df_num.家樂福_400_500>=3) & (df_num.家樂福_400_500<=7), '家樂福_400_500 Class'] = 2
df_num.loc[ (df_num.家樂福_400_500>=8) & (df_num.家樂福_400_500<=14), '家樂福_400_500 Class'] = 3

df_num.loc[ (df_num.家樂福_500_600>=0) & (df_num.家樂福_500_600<=2), '家樂福_500_600 Class'] = 1
df_num.loc[ (df_num.家樂福_500_600>=3) & (df_num.家樂福_500_600<=7), '家樂福_500_600 Class'] = 2
df_num.loc[ (df_num.家樂福_500_600>=8) & (df_num.家樂福_500_600<=14), '家樂福_500_600 Class'] = 3

df_num.loc[ (df_num.家樂福_600_700>=0) & (df_num.家樂福_600_700<=2), '家樂福_600_700 Class'] = 1
df_num.loc[ (df_num.家樂福_600_700>=3) & (df_num.家樂福_600_700<=7), '家樂福_600_700 Class'] = 2
df_num.loc[ (df_num.家樂福_600_700>=8) & (df_num.家樂福_600_700<=14), '家樂福_600_700 Class'] = 3

df_num.loc[ (df_num.家樂福_700_800>=0) & (df_num.家樂福_700_800<=2), '家樂福_700_800 Class'] = 1
df_num.loc[ (df_num.家樂福_700_800>=3) & (df_num.家樂福_700_800<=7), '家樂福_700_800 Class'] = 2
df_num.loc[ (df_num.家樂福_700_800>=8) & (df_num.家樂福_700_800<=14), '家樂福_700_800 Class'] = 3

df_num.loc[ (df_num.家樂福_800_900>=0) & (df_num.家樂福_800_900<=2), '家樂福_800_900 Class'] = 1
df_num.loc[ (df_num.家樂福_800_900>=3) & (df_num.家樂福_800_900<=7), '家樂福_800_900 Class'] = 2
df_num.loc[ (df_num.家樂福_800_900>=8) & (df_num.家樂福_800_900<=14), '家樂福_800_900 Class'] = 3

df_num.loc[ (df_num.家樂福_900_1000>=0) & (df_num.家樂福_900_1000<=2), '家樂福_900_1000 Class'] = 1
df_num.loc[ (df_num.家樂福_900_1000>=3) & (df_num.家樂福_900_1000<=7), '家樂福_900_1000 Class'] = 2
df_num.loc[ (df_num.家樂福_900_1000>=8) & (df_num.家樂福_900_1000<=14), '家樂福_900_1000 Class'] = 3

# 將傳統市場做分組
df_num.loc[ (df_num.傳統市場_0_100>=0) & (df_num.傳統市場_0_100<=4), '傳統市場_0_100 Class'] = 1
df_num.loc[ (df_num.傳統市場_0_100>=5) & (df_num.傳統市場_0_100<=7), '傳統市場_0_100 Class'] = 2
df_num.loc[ (df_num.傳統市場_0_100>=8) & (df_num.傳統市場_0_100<=10), '傳統市場_0_100 Class'] = 3

df_num.loc[ (df_num.傳統市場_100_200>=0) & (df_num.傳統市場_100_200<=4), '傳統市場_100_200 Class'] = 1
df_num.loc[ (df_num.傳統市場_100_200>=5) & (df_num.傳統市場_100_200<=7), '傳統市場_100_200 Class'] = 2
df_num.loc[ (df_num.傳統市場_100_200>=8) & (df_num.傳統市場_100_200<=10), '傳統市場_100_200 Class'] = 3

df_num.loc[ (df_num.傳統市場_200_300>=0) & (df_num.傳統市場_200_300<=4), '傳統市場_200_300 Class'] = 1
df_num.loc[ (df_num.傳統市場_200_300>=5) & (df_num.傳統市場_200_300<=7), '傳統市場_200_300 Class'] = 2
df_num.loc[ (df_num.傳統市場_200_300>=8) & (df_num.傳統市場_200_300<=10), '傳統市場_200_300 Class'] = 3

df_num.loc[ (df_num.傳統市場_300_400>=0) & (df_num.傳統市場_300_400<=4), '傳統市場_300_400 Class'] = 1
df_num.loc[ (df_num.傳統市場_300_400>=5) & (df_num.傳統市場_300_400<=7), '傳統市場_300_400 Class'] = 2
df_num.loc[ (df_num.傳統市場_300_400>=8) & (df_num.傳統市場_300_400<=10), '傳統市場_300_400 Class'] = 3

df_num.loc[ (df_num.傳統市場_400_500>=0) & (df_num.傳統市場_400_500<=4), '傳統市場_400_500 Class'] = 1
df_num.loc[ (df_num.傳統市場_400_500>=5) & (df_num.傳統市場_400_500<=7), '傳統市場_400_500 Class'] = 2
df_num.loc[ (df_num.傳統市場_400_500>=8) & (df_num.傳統市場_400_500<=10), '傳統市場_400_500 Class'] = 3

df_num.loc[ (df_num.傳統市場_500_600>=0) & (df_num.傳統市場_500_600<=4), '傳統市場_500_600 Class'] = 1
df_num.loc[ (df_num.傳統市場_500_600>=5) & (df_num.傳統市場_500_600<=7), '傳統市場_500_600 Class'] = 2
df_num.loc[ (df_num.傳統市場_500_600>=8) & (df_num.傳統市場_500_600<=10), '傳統市場_500_600 Class'] = 3

df_num.loc[ (df_num.傳統市場_600_700>=0) & (df_num.傳統市場_600_700<=4), '傳統市場_600_700 Class'] = 1
df_num.loc[ (df_num.傳統市場_600_700>=5) & (df_num.傳統市場_600_700<=7), '傳統市場_600_700 Class'] = 2
df_num.loc[ (df_num.傳統市場_600_700>=8) & (df_num.傳統市場_600_700<=10), '傳統市場_600_700 Class'] = 3

df_num.loc[ (df_num.傳統市場_700_800>=0) & (df_num.傳統市場_700_800<=4), '傳統市場_700_800 Class'] = 1
df_num.loc[ (df_num.傳統市場_700_800>=5) & (df_num.傳統市場_700_800<=7), '傳統市場_700_800 Class'] = 2
df_num.loc[ (df_num.傳統市場_700_800>=8) & (df_num.傳統市場_700_800<=10), '傳統市場_700_800 Class'] = 3

df_num.loc[ (df_num.傳統市場_800_900>=0) & (df_num.傳統市場_800_900<=4), '傳統市場_800_900 Class'] = 1
df_num.loc[ (df_num.傳統市場_800_900>=5) & (df_num.傳統市場_800_900<=7), '傳統市場_800_900 Class'] = 2
df_num.loc[ (df_num.傳統市場_800_900>=8) & (df_num.傳統市場_800_900<=10), '傳統市場_800_900 Class'] = 3

df_num.loc[ (df_num.傳統市場_900_1000>=0) & (df_num.傳統市場_900_1000<=4), '傳統市場_900_1000 Class'] = 1
df_num.loc[ (df_num.傳統市場_900_1000>=5) & (df_num.傳統市場_900_1000<=7), '傳統市場_900_1000 Class'] = 2
df_num.loc[ (df_num.傳統市場_900_1000>=8) & (df_num.傳統市場_900_1000<=10), '傳統市場_900_1000 Class'] = 3

# 將公車站做分組
df_num.loc[ (df_num.公車站_0_100>=0) & (df_num.公車站_0_100<=8), '公車站_0_100 Class'] = 1
df_num.loc[ (df_num.公車站_0_100>=9) & (df_num.公車站_0_100<=14), '公車站_0_100 Class'] = 2
df_num.loc[ (df_num.公車站_0_100>=15) & (df_num.公車站_0_100<=20), '公車站_0_100 Class'] = 3

df_num.loc[ (df_num.公車站_100_200>=0) & (df_num.公車站_100_200<=8), '公車站_100_200 Class'] = 1
df_num.loc[ (df_num.公車站_100_200>=9) & (df_num.公車站_100_200<=14), '公車站_100_200 Class'] = 2
df_num.loc[ (df_num.公車站_100_200>=15) & (df_num.公車站_100_200<=20), '公車站_100_200 Class'] = 3

df_num.loc[ (df_num.公車站_200_300>=0) & (df_num.公車站_200_300<=8), '公車站_200_300 Class'] = 1
df_num.loc[ (df_num.公車站_200_300>=9) & (df_num.公車站_200_300<=14), '公車站_200_300 Class'] = 2
df_num.loc[ (df_num.公車站_200_300>=15) & (df_num.公車站_200_300<=20), '公車站_200_300 Class'] = 3

df_num.loc[ (df_num.公車站_300_400>=0) & (df_num.公車站_300_400<=8), '公車站_300_400 Class'] = 1
df_num.loc[ (df_num.公車站_300_400>=9) & (df_num.公車站_300_400<=14), '公車站_300_400 Class'] = 2
df_num.loc[ (df_num.公車站_300_400>=15) & (df_num.公車站_300_400<=20), '公車站_300_400 Class'] = 3

df_num.loc[ (df_num.公車站_400_500>=0) & (df_num.公車站_400_500<=8), '公車站_400_500 Class'] = 1
df_num.loc[ (df_num.公車站_400_500>=9) & (df_num.公車站_400_500<=14), '公車站_400_500 Class'] = 2
df_num.loc[ (df_num.公車站_400_500>=15) & (df_num.公車站_400_500<=20), '公車站_400_500 Class'] = 3

df_num.loc[ (df_num.公車站_500_600>=0) & (df_num.公車站_500_600<=8), '公車站_500_600 Class'] = 1
df_num.loc[ (df_num.公車站_500_600>=9) & (df_num.公車站_500_600<=14), '公車站_500_600 Class'] = 2
df_num.loc[ (df_num.公車站_500_600>=15) & (df_num.公車站_500_600<=20), '公車站_500_600 Class'] = 3

df_num.loc[ (df_num.公車站_600_700>=0) & (df_num.公車站_600_700<=8), '公車站_600_700 Class'] = 1
df_num.loc[ (df_num.公車站_600_700>=9) & (df_num.公車站_600_700<=14), '公車站_600_700 Class'] = 2
df_num.loc[ (df_num.公車站_600_700>=15) & (df_num.公車站_600_700<=20), '公車站_600_700 Class'] = 3

df_num.loc[ (df_num.公車站_700_800>=0) & (df_num.公車站_700_800<=8), '公車站_700_800 Class'] = 1
df_num.loc[ (df_num.公車站_700_800>=9) & (df_num.公車站_700_800<=14), '公車站_700_800 Class'] = 2
df_num.loc[ (df_num.公車站_700_800>=15) & (df_num.公車站_700_800<=20), '公車站_700_800 Class'] = 3

df_num.loc[ (df_num.公車站_800_900>=0) & (df_num.公車站_800_900<=8), '公車站_800_900 Class'] = 1
df_num.loc[ (df_num.公車站_800_900>=9) & (df_num.公車站_800_900<=14), '公車站_800_900 Class'] = 2
df_num.loc[ (df_num.公車站_800_900>=15) & (df_num.公車站_800_900<=20), '公車站_800_900 Class'] = 3

df_num.loc[ (df_num.公車站_900_1000>=0) & (df_num.公車站_900_1000<=8), '公車站_900_1000 Class'] = 1
df_num.loc[ (df_num.公車站_900_1000>=9) & (df_num.公車站_900_1000<=14), '公車站_900_1000 Class'] = 2
df_num.loc[ (df_num.公車站_900_1000>=15) & (df_num.公車站_900_1000<=20), '公車站_900_1000 Class'] = 3

# 將捷運站做分組
df_num.loc[ (df_num.捷運站_0_100>=0) & (df_num.捷運站_0_100<=1), '捷運站_0_100 Class'] = 1
df_num.loc[ (df_num.捷運站_0_100==2), '捷運站_0_100 Class'] = 2
df_num.loc[ (df_num.捷運站_0_100==3), '捷運站_0_100 Class'] = 3

df_num.loc[ (df_num.捷運站_100_200>=0) & (df_num.捷運站_100_200<=1), '捷運站_100_200 Class'] = 1
df_num.loc[ (df_num.捷運站_100_200==2), '捷運站_100_200 Class'] = 2
df_num.loc[ (df_num.捷運站_100_200==2), '捷運站_100_200 Class'] = 3

df_num.loc[ (df_num.捷運站_200_300>=0) & (df_num.捷運站_200_300<=1), '捷運站_200_300 Class'] = 1
df_num.loc[ (df_num.捷運站_200_300==2), '捷運站_200_300 Class'] = 2
df_num.loc[ (df_num.捷運站_200_300==2), '捷運站_200_300 Class'] = 3

df_num.loc[ (df_num.捷運站_300_400>=0) & (df_num.捷運站_300_400<=1), '捷運站_300_400 Class'] = 1
df_num.loc[ (df_num.捷運站_300_400==2), '捷運站_300_400 Class'] = 2
df_num.loc[ (df_num.捷運站_300_400==2), '捷運站_300_400 Class'] = 3

df_num.loc[ (df_num.捷運站_400_500>=0) & (df_num.捷運站_400_500<=1), '捷運站_400_500 Class'] = 1
df_num.loc[ (df_num.捷運站_400_500==2), '捷運站_400_500 Class'] = 2
df_num.loc[ (df_num.捷運站_400_500==2), '捷運站_400_500 Class'] = 3

df_num.loc[ (df_num.捷運站_500_600>=0) & (df_num.捷運站_500_600<=1), '捷運站_500_600 Class'] = 1
df_num.loc[ (df_num.捷運站_500_600==2), '捷運站_500_600 Class'] = 2
df_num.loc[ (df_num.捷運站_500_600==2), '捷運站_500_600 Class'] = 3

df_num.loc[ (df_num.捷運站_600_700>=0) & (df_num.捷運站_600_700<=1), '捷運站_600_700 Class'] = 1
df_num.loc[ (df_num.捷運站_600_700==2), '捷運站_600_700 Class'] = 2
df_num.loc[ (df_num.捷運站_600_700==2), '捷運站_600_700 Class'] = 3

df_num.loc[ (df_num.捷運站_700_800>=0) & (df_num.捷運站_700_800<=1), '捷運站_700_800 Class'] = 1
df_num.loc[ (df_num.捷運站_700_800==2), '捷運站_700_800 Class'] = 2
df_num.loc[ (df_num.捷運站_700_800==3), '捷運站_700_800 Class'] = 3

df_num.loc[ (df_num.捷運站_800_900>=0) & (df_num.捷運站_800_900<=1), '捷運站_800_900 Class'] = 1
df_num.loc[ (df_num.捷運站_800_900==2), '捷運站_800_900 Class'] = 2
df_num.loc[ (df_num.捷運站_800_900==2), '捷運站_800_900 Class'] = 3

df_num.loc[ (df_num.捷運站_900_1000>=0) & (df_num.捷運站_900_1000<=1), '捷運站_900_1000 Class'] = 1
df_num.loc[ (df_num.捷運站_900_1000==2), '捷運站_900_1000 Class'] = 2
df_num.loc[ (df_num.捷運站_900_1000==2), '捷運站_900_1000 Class'] = 3

# 將df_num資料切割成df_num_level
df_num_level = df_num.iloc[:,380:760]
# 把df_only_house['單價元平方公尺']放進df_num_level
df_num_level_price = pd.concat([df_num_level, df_only_house.loc[:,'單價元平方公尺']],axis = 1)
df_num_level_price.head()
df_num_level_price.describe()


# # 
# df_num_level_price.corr(method="pearson")
# plt.figure(figsize= (499, 499)) # 圖形大小
# sns.heatmap(df_num_level_price.corr(),annot = True) # 塗顏色
# plt.show()

# sns.pairplot(df_num_level_price)



df_num_level.iloc[:,370:380]
# 將各個Class處理{(0_100)*1.0,(100_200)*0.9,以此類推(900_1000)*0.1}，相加後成一個分數
atm_level = df_num_level['atm_0_100 Class']*1.0 + df_num_level['atm_100_200 Class']*0.9 + df_num_level['atm_200_300 Class']*0.8 + df_num_level['atm_300_400 Class']*0.7 + df_num_level['atm_400_500 Class']*0.6 + df_num_level['atm_500_600 Class']*0.5 + df_num_level['atm_600_700 Class']*0.4 + df_num_level['atm_700_800 Class']*0.3 + df_num_level['atm_800_900 Class']*0.2 + df_num_level['atm_900_1000 Class']*0.1
銀行_level = df_num_level['銀行_0_100 Class']*1.0 + df_num_level['銀行_100_200 Class']*0.9 + df_num_level['銀行_200_300 Class']*0.8 + df_num_level['銀行_300_400 Class']*0.7 + df_num_level['銀行_400_500 Class']*0.6 + df_num_level['銀行_500_600 Class']*0.5 + df_num_level['銀行_600_700 Class']*0.4 + df_num_level['銀行_700_800 Class']*0.3 + df_num_level['銀行_800_900 Class']*0.2 + df_num_level['銀行_900_1000 Class']*0.1
咖啡廳_level = df_num_level['咖啡廳_0_100 Class']*1.0 + df_num_level['咖啡廳_100_200 Class']*0.9 + df_num_level['咖啡廳_200_300 Class']*0.8 + df_num_level['咖啡廳_300_400 Class']*0.7 + df_num_level['咖啡廳_400_500 Class']*0.6 + df_num_level['咖啡廳_500_600 Class']*0.5 + df_num_level['咖啡廳_600_700 Class']*0.4 + df_num_level['咖啡廳_700_800 Class']*0.3 + df_num_level['咖啡廳_800_900 Class']*0.2 + df_num_level['咖啡廳_900_1000 Class']*0.1
便利商店_level = df_num_level['便利商店_0_100 Class']*1.0 + df_num_level['便利商店_100_200 Class']*0.9 + df_num_level['便利商店_200_300 Class']*0.8 + df_num_level['便利商店_300_400 Class']*0.7 + df_num_level['便利商店_400_500 Class']*0.6 + df_num_level['便利商店_500_600 Class']*0.5 + df_num_level['便利商店_600_700 Class']*0.4 + df_num_level['便利商店_700_800 Class']*0.3 + df_num_level['便利商店_800_900 Class']*0.2 + df_num_level['便利商店_900_1000 Class']*0.1
工廠_level = df_num_level['工廠_0_100 Class']*1.0 + df_num_level['工廠_100_200 Class']*0.9 + df_num_level['工廠_200_300 Class']*0.8 + df_num_level['工廠_300_400 Class']*0.7 + df_num_level['工廠_400_500 Class']*0.6 + df_num_level['工廠_500_600 Class']*0.5 + df_num_level['工廠_600_700 Class']*0.4 + df_num_level['工廠_700_800 Class']*0.3 + df_num_level['工廠_800_900 Class']*0.2 + df_num_level['工廠_900_1000 Class']*0.1
麥當勞_level = df_num_level['麥當勞_0_100 Class']*1.0 + df_num_level['麥當勞_100_200 Class']*0.9 + df_num_level['麥當勞_200_300 Class']*0.8 + df_num_level['麥當勞_300_400 Class']*0.7 + df_num_level['麥當勞_400_500 Class']*0.6 + df_num_level['麥當勞_500_600 Class']*0.5 + df_num_level['麥當勞_600_700 Class']*0.4 + df_num_level['麥當勞_700_800 Class']*0.3 + df_num_level['麥當勞_800_900 Class']*0.2 + df_num_level['麥當勞_900_1000 Class']*0.1
肯德基_level = df_num_level['肯德基_0_100 Class']*1.0 + df_num_level['肯德基_100_200 Class']*0.9 + df_num_level['肯德基_200_300 Class']*0.8 + df_num_level['肯德基_300_400 Class']*0.7 + df_num_level['肯德基_400_500 Class']*0.6 + df_num_level['肯德基_500_600 Class']*0.5 + df_num_level['肯德基_600_700 Class']*0.4 + df_num_level['肯德基_700_800 Class']*0.3 + df_num_level['肯德基_800_900 Class']*0.2 + df_num_level['肯德基_900_1000 Class']*0.1
加油站_level = df_num_level['加油站_0_100 Class']*1.0 + df_num_level['加油站_100_200 Class']*0.9 + df_num_level['加油站_200_300 Class']*0.8 + df_num_level['加油站_300_400 Class']*0.7 + df_num_level['加油站_400_500 Class']*0.6 + df_num_level['加油站_500_600 Class']*0.5 + df_num_level['加油站_600_700 Class']*0.4 + df_num_level['加油站_700_800 Class']*0.3 + df_num_level['加油站_800_900 Class']*0.2 + df_num_level['加油站_900_1000 Class']*0.1
健身房_level = df_num_level['健身房_0_100 Class']*1.0 + df_num_level['健身房_100_200 Class']*0.9 + df_num_level['健身房_200_300 Class']*0.8 + df_num_level['健身房_300_400 Class']*0.7 + df_num_level['健身房_400_500 Class']*0.6 + df_num_level['健身房_500_600 Class']*0.5 + df_num_level['健身房_600_700 Class']*0.4 + df_num_level['健身房_700_800 Class']*0.3 + df_num_level['健身房_800_900 Class']*0.2 + df_num_level['健身房_900_1000 Class']*0.1
國民運動中心_level = df_num_level['國民運動中心_0_100 Class']*1.0 + df_num_level['國民運動中心_100_200 Class']*0.9 + df_num_level['國民運動中心_200_300 Class']*0.8 + df_num_level['國民運動中心_300_400 Class']*0.7 + df_num_level['國民運動中心_400_500 Class']*0.6 + df_num_level['國民運動中心_500_600 Class']*0.5 + df_num_level['國民運動中心_600_700 Class']*0.4 + df_num_level['國民運動中心_700_800 Class']*0.3 + df_num_level['國民運動中心_800_900 Class']*0.2 + df_num_level['國民運動中心_900_1000 Class']*0.1
五金百貨_level = df_num_level['五金百貨_0_100 Class']*1.0 + df_num_level['五金百貨_100_200 Class']*0.9 + df_num_level['五金百貨_200_300 Class']*0.8 + df_num_level['五金百貨_300_400 Class']*0.7 + df_num_level['五金百貨_400_500 Class']*0.6 + df_num_level['五金百貨_500_600 Class']*0.5 + df_num_level['五金百貨_600_700 Class']*0.4 + df_num_level['五金百貨_700_800 Class']*0.3 + df_num_level['五金百貨_800_900 Class']*0.2 + df_num_level['五金百貨_900_1000 Class']*0.1
醫院_level = df_num_level['醫院_0_100 Class']*1.0 + df_num_level['醫院_100_200 Class']*0.9 + df_num_level['醫院_200_300 Class']*0.8 + df_num_level['醫院_300_400 Class']*0.7 + df_num_level['醫院_400_500 Class']*0.6 + df_num_level['醫院_500_600 Class']*0.5 + df_num_level['醫院_600_700 Class']*0.4 + df_num_level['醫院_700_800 Class']*0.3 + df_num_level['醫院_800_900 Class']*0.2 + df_num_level['醫院_900_1000 Class']*0.1
診所_level = df_num_level['診所_0_100 Class']*1.0 + df_num_level['診所_100_200 Class']*0.9 + df_num_level['診所_200_300 Class']*0.8 + df_num_level['診所_300_400 Class']*0.7 + df_num_level['診所_400_500 Class']*0.6 + df_num_level['診所_500_600 Class']*0.5 + df_num_level['診所_600_700 Class']*0.4 + df_num_level['診所_700_800 Class']*0.3 + df_num_level['診所_800_900 Class']*0.2 + df_num_level['診所_900_1000 Class']*0.1
圖書館_level = df_num_level['圖書館_0_100 Class']*1.0 + df_num_level['圖書館_100_200 Class']*0.9 + df_num_level['圖書館_200_300 Class']*0.8 + df_num_level['圖書館_300_400 Class']*0.7 + df_num_level['圖書館_400_500 Class']*0.6 + df_num_level['圖書館_500_600 Class']*0.5 + df_num_level['圖書館_600_700 Class']*0.4 + df_num_level['圖書館_700_800 Class']*0.3 + df_num_level['圖書館_800_900 Class']*0.2 + df_num_level['圖書館_900_1000 Class']*0.1
超市_level = df_num_level['超市_0_100 Class']*1.0 + df_num_level['超市_100_200 Class']*0.9 + df_num_level['超市_200_300 Class']*0.8 + df_num_level['超市_300_400 Class']*0.7 + df_num_level['超市_400_500 Class']*0.6 + df_num_level['超市_500_600 Class']*0.5 + df_num_level['超市_600_700 Class']*0.4 + df_num_level['超市_700_800 Class']*0.3 + df_num_level['超市_800_900 Class']*0.2 + df_num_level['超市_900_1000 Class']*0.1
電影院_level = df_num_level['電影院_0_100 Class']*1.0 + df_num_level['電影院_100_200 Class']*0.9 + df_num_level['電影院_200_300 Class']*0.8 + df_num_level['電影院_300_400 Class']*0.7 + df_num_level['電影院_400_500 Class']*0.6 + df_num_level['電影院_500_600 Class']*0.5 + df_num_level['電影院_600_700 Class']*0.4 + df_num_level['電影院_700_800 Class']*0.3 + df_num_level['電影院_800_900 Class']*0.2 + df_num_level['電影院_900_1000 Class']*0.1
博物館_level = df_num_level['博物館_0_100 Class']*1.0 + df_num_level['博物館_100_200 Class']*0.9 + df_num_level['博物館_200_300 Class']*0.8 + df_num_level['博物館_300_400 Class']*0.7 + df_num_level['博物館_400_500 Class']*0.6 + df_num_level['博物館_500_600 Class']*0.5 + df_num_level['博物館_600_700 Class']*0.4 + df_num_level['博物館_700_800 Class']*0.3 + df_num_level['博物館_800_900 Class']*0.2 + df_num_level['博物館_900_1000 Class']*0.1
美術館_level = df_num_level['美術館_0_100 Class']*1.0 + df_num_level['美術館_100_200 Class']*0.9 + df_num_level['美術館_200_300 Class']*0.8 + df_num_level['美術館_300_400 Class']*0.7 + df_num_level['美術館_400_500 Class']*0.6 + df_num_level['美術館_500_600 Class']*0.5 + df_num_level['美術館_600_700 Class']*0.4 + df_num_level['美術館_700_800 Class']*0.3 + df_num_level['美術館_800_900 Class']*0.2 + df_num_level['美術館_900_1000 Class']*0.1
夜市_level = df_num_level['夜市_0_100 Class']*1.0 + df_num_level['夜市_100_200 Class']*0.9 + df_num_level['夜市_200_300 Class']*0.8 + df_num_level['夜市_300_400 Class']*0.7 + df_num_level['夜市_400_500 Class']*0.6 + df_num_level['夜市_500_600 Class']*0.5 + df_num_level['夜市_600_700 Class']*0.4 + df_num_level['夜市_700_800 Class']*0.3 + df_num_level['夜市_800_900 Class']*0.2 + df_num_level['夜市_900_1000 Class']*0.1
公園_level = df_num_level['公園_0_100 Class']*1.0 + df_num_level['公園_100_200 Class']*0.9 + df_num_level['公園_200_300 Class']*0.8 + df_num_level['公園_300_400 Class']*0.7 + df_num_level['公園_400_500 Class']*0.6 + df_num_level['公園_500_600 Class']*0.5 + df_num_level['公園_600_700 Class']*0.4 + df_num_level['公園_700_800 Class']*0.3 + df_num_level['公園_800_900 Class']*0.2 + df_num_level['公園_900_1000 Class']*0.1
停車場_level = df_num_level['停車場_0_100 Class']*1.0 + df_num_level['停車場_100_200 Class']*0.9 + df_num_level['停車場_200_300 Class']*0.8 + df_num_level['停車場_300_400 Class']*0.7 + df_num_level['停車場_400_500 Class']*0.6 + df_num_level['停車場_500_600 Class']*0.5 + df_num_level['停車場_600_700 Class']*0.4 + df_num_level['停車場_700_800 Class']*0.3 + df_num_level['停車場_800_900 Class']*0.2 + df_num_level['停車場_900_1000 Class']*0.1
餐廳_level = df_num_level['餐廳_0_100 Class']*1.0 + df_num_level['餐廳_100_200 Class']*0.9 + df_num_level['餐廳_200_300 Class']*0.8 + df_num_level['餐廳_300_400 Class']*0.7 + df_num_level['餐廳_400_500 Class']*0.6 + df_num_level['餐廳_500_600 Class']*0.5 + df_num_level['餐廳_600_700 Class']*0.4 + df_num_level['餐廳_700_800 Class']*0.3 + df_num_level['餐廳_800_900 Class']*0.2 + df_num_level['餐廳_900_1000 Class']*0.1
景點_level = df_num_level['景點_0_100 Class']*1.0 + df_num_level['景點_100_200 Class']*0.9 + df_num_level['景點_200_300 Class']*0.8 + df_num_level['景點_300_400 Class']*0.7 + df_num_level['景點_400_500 Class']*0.6 + df_num_level['景點_500_600 Class']*0.5 + df_num_level['景點_600_700 Class']*0.4 + df_num_level['景點_700_800 Class']*0.3 + df_num_level['景點_800_900 Class']*0.2 + df_num_level['景點_900_1000 Class']*0.1
幼稚園_level = df_num_level['幼稚園_0_100 Class']*1.0 + df_num_level['幼稚園_100_200 Class']*0.9 + df_num_level['幼稚園_200_300 Class']*0.8 + df_num_level['幼稚園_300_400 Class']*0.7 + df_num_level['幼稚園_400_500 Class']*0.6 + df_num_level['幼稚園_500_600 Class']*0.5 + df_num_level['幼稚園_600_700 Class']*0.4 + df_num_level['幼稚園_700_800 Class']*0.3 + df_num_level['幼稚園_800_900 Class']*0.2 + df_num_level['幼稚園_900_1000 Class']*0.1
國小_level = df_num_level['國小_0_100 Class']*1.0 + df_num_level['國小_100_200 Class']*0.9 + df_num_level['國小_200_300 Class']*0.8 + df_num_level['國小_300_400 Class']*0.7 + df_num_level['國小_400_500 Class']*0.6 + df_num_level['國小_500_600 Class']*0.5 + df_num_level['國小_600_700 Class']*0.4 + df_num_level['國小_700_800 Class']*0.3 + df_num_level['國小_800_900 Class']*0.2 + df_num_level['國小_900_1000 Class']*0.1
國中_level = df_num_level['國中_0_100 Class']*1.0 + df_num_level['國中_100_200 Class']*0.9 + df_num_level['國中_200_300 Class']*0.8 + df_num_level['國中_300_400 Class']*0.7 + df_num_level['國中_400_500 Class']*0.6 + df_num_level['國中_500_600 Class']*0.5 + df_num_level['國中_600_700 Class']*0.4 + df_num_level['國中_700_800 Class']*0.3 + df_num_level['國中_800_900 Class']*0.2 + df_num_level['國中_900_1000 Class']*0.1
高中_level = df_num_level['高中_0_100 Class']*1.0 + df_num_level['高中_100_200 Class']*0.9 + df_num_level['高中_200_300 Class']*0.8 + df_num_level['高中_300_400 Class']*0.7 + df_num_level['高中_400_500 Class']*0.6 + df_num_level['高中_500_600 Class']*0.5 + df_num_level['高中_600_700 Class']*0.4 + df_num_level['高中_700_800 Class']*0.3 + df_num_level['高中_800_900 Class']*0.2 + df_num_level['高中_900_1000 Class']*0.1
高職_level = df_num_level['高職_0_100 Class']*1.0 + df_num_level['高職_100_200 Class']*0.9 + df_num_level['高職_200_300 Class']*0.8 + df_num_level['高職_300_400 Class']*0.7 + df_num_level['高職_400_500 Class']*0.6 + df_num_level['高職_500_600 Class']*0.5 + df_num_level['高職_600_700 Class']*0.4 + df_num_level['高職_700_800 Class']*0.3 + df_num_level['高職_800_900 Class']*0.2 + df_num_level['高職_900_1000 Class']*0.1
大學_level = df_num_level['大學_0_100 Class']*1.0 + df_num_level['大學_100_200 Class']*0.9 + df_num_level['大學_200_300 Class']*0.8 + df_num_level['大學_300_400 Class']*0.7 + df_num_level['大學_400_500 Class']*0.6 + df_num_level['大學_500_600 Class']*0.5 + df_num_level['大學_600_700 Class']*0.4 + df_num_level['大學_700_800 Class']*0.3 + df_num_level['大學_800_900 Class']*0.2 + df_num_level['大學_900_1000 Class']*0.1
科大_level = df_num_level['科大_0_100 Class']*1.0 + df_num_level['科大_100_200 Class']*0.9 + df_num_level['科大_200_300 Class']*0.8 + df_num_level['科大_300_400 Class']*0.7 + df_num_level['科大_400_500 Class']*0.6 + df_num_level['科大_500_600 Class']*0.5 + df_num_level['科大_600_700 Class']*0.4 + df_num_level['科大_700_800 Class']*0.3 + df_num_level['科大_800_900 Class']*0.2 + df_num_level['科大_900_1000 Class']*0.1
學校_level = df_num_level['學校_0_100 Class']*1.0 + df_num_level['學校_100_200 Class']*0.9 + df_num_level['學校_200_300 Class']*0.8 + df_num_level['學校_300_400 Class']*0.7 + df_num_level['學校_400_500 Class']*0.6 + df_num_level['學校_500_600 Class']*0.5 + df_num_level['學校_600_700 Class']*0.4 + df_num_level['學校_700_800 Class']*0.3 + df_num_level['學校_800_900 Class']*0.2 + df_num_level['學校_900_1000 Class']*0.1
商圈_level = df_num_level['商圈_0_100 Class']*1.0 + df_num_level['商圈_100_200 Class']*0.9 + df_num_level['商圈_200_300 Class']*0.8 + df_num_level['商圈_300_400 Class']*0.7 + df_num_level['商圈_400_500 Class']*0.6 + df_num_level['商圈_500_600 Class']*0.5 + df_num_level['商圈_600_700 Class']*0.4 + df_num_level['商圈_700_800 Class']*0.3 + df_num_level['商圈_800_900 Class']*0.2 + df_num_level['商圈_900_1000 Class']*0.1
星巴克_level = df_num_level['星巴克_0_100 Class']*1.0 + df_num_level['星巴克_100_200 Class']*0.9 + df_num_level['星巴克_200_300 Class']*0.8 + df_num_level['星巴克_300_400 Class']*0.7 + df_num_level['星巴克_400_500 Class']*0.6 + df_num_level['星巴克_500_600 Class']*0.5 + df_num_level['星巴克_600_700 Class']*0.4 + df_num_level['星巴克_700_800 Class']*0.3 + df_num_level['星巴克_800_900 Class']*0.2 + df_num_level['星巴克_900_1000 Class']*0.1
大潤發_level = df_num_level['大潤發_0_100 Class']*1.0 + df_num_level['大潤發_100_200 Class']*0.9 + df_num_level['大潤發_200_300 Class']*0.8 + df_num_level['大潤發_300_400 Class']*0.7 + df_num_level['大潤發_400_500 Class']*0.6 + df_num_level['大潤發_500_600 Class']*0.5 + df_num_level['大潤發_600_700 Class']*0.4 + df_num_level['大潤發_700_800 Class']*0.3 + df_num_level['大潤發_800_900 Class']*0.2 + df_num_level['大潤發_900_1000 Class']*0.1
家樂福_level = df_num_level['家樂福_0_100 Class']*1.0 + df_num_level['家樂福_100_200 Class']*0.9 + df_num_level['家樂福_200_300 Class']*0.8 + df_num_level['家樂福_300_400 Class']*0.7 + df_num_level['家樂福_400_500 Class']*0.6 + df_num_level['家樂福_500_600 Class']*0.5 + df_num_level['家樂福_600_700 Class']*0.4 + df_num_level['家樂福_700_800 Class']*0.3 + df_num_level['家樂福_800_900 Class']*0.2 + df_num_level['家樂福_900_1000 Class']*0.1
傳統市場_level = df_num_level['傳統市場_0_100 Class']*1.0 + df_num_level['傳統市場_100_200 Class']*0.9 + df_num_level['傳統市場_200_300 Class']*0.8 + df_num_level['傳統市場_300_400 Class']*0.7 + df_num_level['傳統市場_400_500 Class']*0.6 + df_num_level['傳統市場_500_600 Class']*0.5 + df_num_level['傳統市場_600_700 Class']*0.4 + df_num_level['傳統市場_700_800 Class']*0.3 + df_num_level['傳統市場_800_900 Class']*0.2 + df_num_level['傳統市場_900_1000 Class']*0.1
公車站_level = df_num_level['公車站_0_100 Class']*1.0 + df_num_level['公車站_100_200 Class']*0.9 + df_num_level['公車站_200_300 Class']*0.8 + df_num_level['公車站_300_400 Class']*0.7 + df_num_level['公車站_400_500 Class']*0.6 + df_num_level['公車站_500_600 Class']*0.5 + df_num_level['公車站_600_700 Class']*0.4 + df_num_level['公車站_700_800 Class']*0.3 + df_num_level['公車站_800_900 Class']*0.2 + df_num_level['公車站_900_1000 Class']*0.1
捷運站_level = df_num_level['捷運站_0_100 Class']*1.0 + df_num_level['捷運站_100_200 Class']*0.9 + df_num_level['捷運站_200_300 Class']*0.8 + df_num_level['捷運站_300_400 Class']*0.7 + df_num_level['捷運站_400_500 Class']*0.6 + df_num_level['捷運站_500_600 Class']*0.5 + df_num_level['捷運站_600_700 Class']*0.4 + df_num_level['捷運站_700_800 Class']*0.3 + df_num_level['捷運站_800_900 Class']*0.2 + df_num_level['捷運站_900_1000 Class']*0.1

df_level = pd.concat([atm_level,銀行_level,咖啡廳_level,便利商店_level,工廠_level,麥當勞_level,肯德基_level,加油站_level,健身房_level,國民運動中心_level,五金百貨_level,醫院_level,診所_level,圖書館_level,超市_level,電影院_level,博物館_level,美術館_level,夜市_level,公園_level,停車場_level,餐廳_level,景點_level,幼稚園_level,國小_level,國中_level,高中_level,高職_level,大學_level,科大_level,學校_level,商圈_level,星巴克_level,大潤發_level,家樂福_level,傳統市場_level,公車站_level,捷運站_level,df_only_house.loc[:,'單價元平方公尺'],df_nearest_avg_price.loc[:,'最近建物的單價元平方公尺']],axis = 1)
df_level.columns = ['atm','bank','Cafe','convenience store','factory','McDonald','KFC','Gas station','GYM','National Sports Center','hardware department store','hospital','Clinic','library','supermarket','Cinema','museum','art gallery','night market','public park','parking lot','restaurant','Attractions','kindergarten','elementary school','secondary','high school','Higher vocational','University','University of Technology','School','business district','Starbucks','RT-Mart','Carrefour','traditional market','bus station','MRT','unit price per square meter','nearest_avg_price']
df_level.to_csv("chungli_density_level_ML.csv", index = False,encoding="utf_8_sig")


# # 用seaborn觀察各資料與每平方公尺單價的關係
# sns.jointplot(df_level['atm'],df_level['unit price per square meter'])
# sns.jointplot(df_level['bank'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Cafe'],df_level['unit price per square meter'])
# sns.jointplot(df_level['convenience store'],df_level['unit price per square meter'])
# sns.jointplot(df_level['factory'],df_level['unit price per square meter'])
# sns.jointplot(df_level['McDonald'],df_level['unit price per square meter'])
# sns.jointplot(df_level['KFC'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Gas station'],df_level['unit price per square meter'])
# sns.jointplot(df_level['GYM'],df_level['unit price per square meter'])
# sns.jointplot(df_level['National Sports Center'],df_level['unit price per square meter'])
# sns.jointplot(df_level['hardware department store'],df_level['unit price per square meter'])
# sns.jointplot(df_level['hospital'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Clinic'],df_level['unit price per square meter'])
# sns.jointplot(df_level['library'],df_level['unit price per square meter'])
# sns.jointplot(df_level['supermarket'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Cinema'],df_level['unit price per square meter'])
# sns.jointplot(df_level['museum'],df_level['unit price per square meter'])
# sns.jointplot(df_level['art gallery'],df_level['unit price per square meter'])
# sns.jointplot(df_level['night market'],df_level['unit price per square meter'])
# sns.jointplot(df_level['public park'],df_level['unit price per square meter'])
# sns.jointplot(df_level['parking lot'],df_level['unit price per square meter'])
# sns.jointplot(df_level['restaurant'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Attractions'],df_level['unit price per square meter'])
# sns.jointplot(df_level['kindergarten'],df_level['unit price per square meter'])
# sns.jointplot(df_level['elementary school'],df_level['unit price per square meter'])
# sns.jointplot(df_level['secondary'],df_level['unit price per square meter'])
# sns.jointplot(df_level['high school'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Higher vocational'],df_level['unit price per square meter'])
# sns.jointplot(df_level['University'],df_level['unit price per square meter'])
# sns.jointplot(df_level['University of Technology'],df_level['unit price per square meter'])
# sns.jointplot(df_level['School'],df_level['unit price per square meter'])
# sns.jointplot(df_level['business district'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Starbucks'],df_level['unit price per square meter'])
# sns.jointplot(df_level['RT-Mart'],df_level['unit price per square meter'])
# sns.jointplot(df_level['Carrefour'],df_level['unit price per square meter'])
# sns.jointplot(df_level['traditional market'],df_level['unit price per square meter'])
# sns.jointplot(df_level['bus station'],df_level['unit price per square meter'])
# sns.jointplot(df_level['MRT'],df_level['unit price per square meter'])
# sns.jointplot(df_level['nearest_avg_price'],df_level['unit price per square meter'])



# n = range(1,11)
# k = range(10)
# m = range(0,380,10)
# for i in range(len(df_num_level)):
#     a = df_num_level.iloc[:,0+k+m] * n
#     print(a)

# train model

from sklearn.linear_model import LinearRegression

X = df_level.drop(['unit price per square meter'],axis=1)
# X = df_num_level_price.iloc[:,[210,220,310,330]]
#y是目標值
y = df_level['unit price per square meter']
#split to training data & testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=54)

#using linear regression model
reg = LinearRegression()
reg.fit(X_train, y_train)
#get the result
predictions = reg.predict(X_test)

from sklearn.metrics import r2_score
r2_score(y_test, predictions)
plt.scatter(y_test, predictions, color='blue')


# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score, recall_score, precision_score
# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)
# recall = recall_score(y_test, predictions)
# precision = precision_score(y_test, predictions)

#Export model
import joblib
joblib.dump(reg,'house_price_predict_density_2022_06_02_Wang.pkl',compress=3)

