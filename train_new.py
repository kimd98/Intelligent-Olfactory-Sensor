import numpy as np
import pandas as pd

## Importing files

# all data
# citrus : /content/drive/MyDrive/data/citrus/citrus0.csv
citrusList = []
for i in range(10):
    citrusList.append(pd.read_csv("/content/drive/MyDrive/data/citrus/citrus{}.csv".format(i), header=None))

citrus = pd.concat(citrusList)
citrus['label'] = 0

# fish : /content/drive/MyDrive/data/fish/fish0.csv
fishList = []
for i in range(10):
    fishList.append(pd.read_csv("/content/drive/MyDrive/data/fish/fish{}.csv".format(i), header=None))

fish = pd.concat(fishList)
fish['label'] = 1

FAList = []
for i in range(10):
    FAList.append(pd.read_csv("/content/drive/MyDrive/data/freshair/freshair{}.csv".format(i), header=None))

FA = pd.concat(FAList)
FA['label'] = 2

PMList = []
for i in range(10):
    PMList.append(pd.read_csv("/content/drive/MyDrive/data/peppermint/peppermint{}.csv".format(i), header=None))

PM = pd.concat(PMList)
PM['label'] = 3

citrus

## Now you have 4 diffrent lists of size 160 each, next step is to join them.
df = pd.concat([PM, FA, fish, citrus])

## now your final df should have 160*4 rows?
df.describe()

df.head(100)

"""## Data Description
Labels:

* citrus: 0
* fish: 1
* freshair: 2
* pepermint: 3

We have 640 rows. Usually people do 80:20 split. I belive transforming the data was the most dificult (Its like 80% of the work in any ML project) part rest should be straight forward.

I have just joined all the data in variable 'df'. it contains 640 rows.
"""

## split the data 
from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2)

import tensorflow as tf

from tensorflow import feature_column
from tensorflow.keras import layers

# A utility method to create a tf.data dataset from a Pandas Dataframe
def df_to_dataset(dataframe, shuffle=True, batch_size=32):
  dataframe = dataframe.copy()
  labels = dataframe.pop('label')
  ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  return ds

batch_size = 5 # A small batch sized is used for demonstration purposes
train_ds = df_to_dataset(train, batch_size=batch_size)
test_ds = df_to_dataset(test, shuffle=False, batch_size=batch_size)



"""# SKLEARN"""

# sklearn technique
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df.drop("label", axis = 1)
y = df.label

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.8)
model = RandomForestClassifier(n_estimators=100, max_depth=10)
model.fit(X_train, y_train)

t_score = model.score(X_train, y_train)
v_score = model.score(X_valid, y_valid)

print("Train Score:", t_score)
print("Test Score:", v_score)

# DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.8)
model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)

t_score = model.score(X_train, y_train)
v_score = model.score(X_valid, y_valid)

print("Train Score:", t_score)
print("Test Score:", v_score)
