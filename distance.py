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
df_dis = pd.read_csv(r'dis_all.csv', encoding = 'utf_8_sig')
df_only_house = pd.read_csv(r'real_price_only_house_chungli.csv', encoding = 'utf_8_sig')
df_nearest_avg_price = pd.read_csv(r'real_price_only_house_chungli_price.csv', encoding = 'utf_8_sig')

#observing dataset
df_dis.head()
df_dis.describe()
df_dis.info()


# 將df_num資料切割成df_num_level
df_dis_dis = df_dis.iloc[:,[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]]
# 把df_only_house['單價元平方公尺']放進df_num_level
df_dis_price = pd.concat([df_dis_dis,df_only_house.loc[:,'單價元平方公尺'],df_nearest_avg_price.loc[:,'最近建物的單價元平方公尺']],axis = 1)
# df_dis_dis_price = pd.concat([df_dis_dis, df_chungli.iloc[:,'最近建物的單價元平方公尺']],axis = 1)

from sklearn.linear_model import LinearRegression

X = df_dis_price.drop(['單價元平方公尺'],axis=1)
y = df_dis_price['單價元平方公尺']
#split to training data & testing data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=45)

#using linear regression model
reg = LinearRegression()
reg.fit(X_train, y_train)
#get the result
predictions = reg.predict(X_test)

from sklearn.metrics import r2_score
r2_score(y_test, predictions)
plt.scatter(y_test, predictions, color='blue')

df_dis_price.columns = ['art gallery','bus station','convenience store','department store','Interchange','HSR','library','supermarket','Cinema','MRT','museum','night market','School','business district','vegetable market','train station','unit price per square meter','nearest_avg_price']
df_dis_price.to_csv("chungli_distance_ML.csv", index = False,encoding="utf_8_sig")

# # 作圖分析
# sns.jointplot(df_dis_price['art gallery'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['bus station'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['convenience store'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['department store'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['Interchange'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['HSR'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['library'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['supermarket'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['Cinema'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['MRT'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['museum'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['night market'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['School'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['business district'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['vegetable market'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['train station'],df_dis_price['unit price per square meter'])
# sns.jointplot(df_dis_price['nearest_avg_price'],df_dis_price['unit price per square meter'])




#Export model
import joblib
joblib.dump(reg,'house_distance_price_predict_2022_05_29_Wang.pkl',compress=3)

