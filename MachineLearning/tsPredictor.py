import pandas as pd
import numpy as np
from itertools import combinations,permutations
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor 
from sklearn.metrics import mean_absolute_error as mae

file_location = r'C:\Users\rohan\Downloads\finaldata_alloy_comp.csv'
data = pd.read_csv(file_location)

# print data.head()

def wt():
    weights = np.random.random(3)
    weights /= weights.sum();weights*=100;weights = weights.round(2)
    return weights

metals = []
for column in 'm1 m2 m3 m4 m5 m6 m7 m8 m9 m10 m11'.split(' '):
    metals.extend(data[column].drop_duplicates().dropna())

metals = np.asarray(list(set(metals)))

metals[metals!='nan']
metals.sort()

new_comps = []
for i in combinations(metals,3):
    new_comps.append(','.join([m+str(n) for m,n in zip(i,wt())]))
# print('Number of new randomly generated components:',len(new_comps))

new = pd.DataFrame({'composition':new_comps})
expanded = new['composition'].str.split(',', expand=True)

for column in expanded.columns:
     m = expanded[column].str.extract(r'([a-zA-Z]+)([0-9\.]+)')
     m.columns = ['m'+str(column+1),'m'+str(column+1)+'%']
     m['m'+str(column+1)+'%'] = m['m'+str(column+1)+'%'].astype('float')
     new = pd.concat([new,m],axis='columns')

# print new.head()
# print new.tail()

data1 = pd.concat([data,new],sort=False)

# print data1.head()
# print data1.tail()

for col in 'm1 m2 m3 m4 m5 m6 m7 m8 m9 m10 m11'.split(' '):
    data1[col] = data1[col].astype('category')

# print data1.head()

df = pd.get_dummies(data1.drop(['composition'],axis='columns'))

# print df.head()

df.fillna(0,inplace=True)
# print df.head()

new_dum = df[df['TS'] == 0]
df = df[df['TS'] != 0]
new_dum.drop(['TS'],axis='columns',inplace=True)

# print new_dum.head()

X = df.drop(['TS'],axis='columns')
y = df['TS']

tsize = 0.9
print('Test Size: ',tsize)
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=0,test_size=tsize)

data.loc[X_train.index]['composition']
data.loc[X_test.index]['composition']

rf = RandomForestRegressor(bootstrap=True, max_depth=None,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_decrease=9, min_impurity_split=None,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, n_estimators=10, n_jobs=1,
           oob_score=False, random_state=0, verbose=0, warm_start=False)

rf.fit(X_train,y_train)

rf_train_preds = rf.predict(X_train)
print('RF train error: ',mae(y_train,rf_train_preds))

rf_test_preds = rf.predict(X_test)
print('RF test error : ',mae(y_test,rf_test_preds))