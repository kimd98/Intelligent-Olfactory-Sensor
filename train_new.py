import numpy as np
import pandas as pd

## Importing files

# all data
# citrus : /content/drive/MyDrive/data/citrus/citrus0.csv
citrusList = []
for i in range(10):
    citrusList.append(pd.read_csv("data/citrus/citrus{}.csv".format(i), header=None))

citrus = pd.concat(citrusList)
citrus['label'] = 0

# fish : /content/drive/MyDrive/data/fish/fish0.csv
fishList = []
for i in range(10):
    fishList.append(pd.read_csv("data/fish/fish{}.csv".format(i), header=None))

fish = pd.concat(fishList)
fish['label'] = 1

FAList = []
for i in range(10):
    FAList.append(pd.read_csv("data/freshair/freshair{}.csv".format(i), header=None))

FA = pd.concat(FAList)
FA['label'] = 2

PMList = []
for i in range(10):
    PMList.append(pd.read_csv("data/peppermint/peppermint{}.csv".format(i), header=None))

PM = pd.concat(PMList)
PM['label'] = 3

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
"""

X = df.drop("label", axis = 1)
y = df.label

# DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.8)
model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)

t_score = model.score(X_train, y_train)
v_score = model.score(X_valid, y_valid)

print("Train Score:", t_score)
print("Test Score:", v_score)
