import os
import numpy as np
import pandas as pd

## Importing csv files

# freshair (0): room, outside
FAlist = []
FARpath = '/content/drive/MyDrive/SGP40/data/freshair/FA_room'
FAOpath = '/content/drive/MyDrive/SGP40/data/freshair/FA_outside'
for f in os.listdir(FARpath):
    FAlist.append(pd.read_csv(os.path.join(FARpath, f), header=None))
for f in os.listdir(FAOpath):
    FAlist.append(pd.read_csv(os.path.join(FAOpath, f), header=None))
FA = pd.concat(FAlist)
FA['label'] = 0

## banana (non-citrus fruity) vs citrus (citrus fruity)

# banana (1): air, container
BAlist = []
BApath = '/content/drive/MyDrive/SGP40/data/banana/BA_air'
BCpath = '/content/drive/MyDrive/SGP40/data/banana/BA_container'
for f in os.listdir(BApath):
    BAlist.append(pd.read_csv(os.path.join(BApath, f), header=None))
for f in os.listdir(BCpath):
    BAlist.append(pd.read_csv(os.path.join(BCpath, f), header=None))
BA = pd.concat(BAlist)
BA['label'] = 1

## citrusP (citrus fragent) vs citrusM (citrus sweet)

# citrus_perfume (2)
citrusPlist = []
citrusPpath = '/content/drive/MyDrive/SGP40/data/citrus/citrus_perfume'
for f in os.listdir(citrusPpath):
    citrusPlist.append(pd.read_csv(os.path.join(citrusPpath, f), header=None))
citrusP = pd.concat(citrusPlist)
citrusP['label'] = 2

# citrus_mandarine (3)
citrusMlist = []
citrusMpath = '/content/drive/MyDrive/SGP40/data/citrus/citrus_mandarine'
for f in os.listdir(citrusMpath):
    citrusMlist.append(pd.read_csv(os.path.join(citrusMpath, f), header=None))
citrusM = pd.concat(citrusMlist)
citrusM['label'] = 3

## fish (decayed) vs garlic (pungent)

# fish (4): container, air
fishlist = []
fishCpath = '/content/drive/MyDrive/SGP40/data/fish/fish_container'
fishApath = '/content/drive/MyDrive/SGP40/data/fish/fish_air'
for f in os.listdir(fishCpath):
    fishlist.append(pd.read_csv(os.path.join(fishCpath, f), header=None))
for f in os.listdir(fishApath):
    fishlist.append(pd.read_csv(os.path.join(fishApath, f), header=None))
fish = pd.concat(fishlist)
fish['label'] = 4

# garlic (5): container, air
Glist = []
GApath = '/content/drive/MyDrive/SGP40/data/garlic/garlic_air'
GCpath = '/content/drive/MyDrive/SGP40/data/garlic/garlic_container'
for f in os.listdir(GApath):
    Glist.append(pd.read_csv(os.path.join(GApath, f), header=None))
for f in os.listdir(GCpath):
    Glist.append(pd.read_csv(os.path.join(GCpath, f), header=None))
garlic = pd.concat(Glist)
garlic['label'] = 5

## peppermint (minty, mentholic herbal)

# peppermint (6): container, air
PMlist = []
PMApath = '/content/drive/MyDrive/SGP40/data/peppermint/PM_air'
PMCpath = '/content/drive/MyDrive/SGP40/data/peppermint/PM_container'
for f in os.listdir(PMApath):
    PMlist.append(pd.read_csv(os.path.join(PMApath, f), header=None))
for f in os.listdir(PMCpath):
    PMlist.append(pd.read_csv(os.path.join(PMCpath, f), header=None))
PM = pd.concat(PMlist)
PM['label'] = 6

df = pd.concat([FA, BA, citrusP, citrusM, fish, garlic, PM])
# print(df.describe())
# print(df.head(100))

X = df.drop("label", axis = 1)
y = df.label

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# train 80, test 20
X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=0.8)
model = DecisionTreeClassifier(max_depth=10)
model.fit(X_train, y_train)

t_score = model.score(X_train, y_train)
v_score = model.score(X_valid, y_valid)

print("Train Score:", t_score)
print("Test Score:", v_score)
