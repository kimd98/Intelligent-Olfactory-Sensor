import os
import numpy as np
import tensorflow as tf

# names of data types
data1 = 'freshair'
data2 = 'citrus'
data3 = 'peppermint'
data4 = 'fish'
data_num = 4

# data path
data_dir = 'data'
data_path1 = data_dir + '/' + data1
data_path2 = data_dir + '/' + data2
data_path3 = data_dir + '/' + data3
data_path4 = data_dir + '/' + data4
test_path = data_dir + '/test'

# datasets of all files matching patterns
dataset1 = os.listdir(data_path1)
dataset2 = os.listdir(data_path2)
dataset3 = os.listdir(data_path3)
dataset4 = os.listdir(data_path4)

# lists of data labels (rank-1 tensors)
label1 = np.full(len(dataset1), data1)
label2 = np.full(len(dataset2), data2)
label3 = np.full(len(dataset3), data3)
label4 = np.full(len(dataset4), data4)

# create a label set and convert to a rank-2 tensor
train_label = (label1, label2, label3, label4)
train_label = np.stack(train_label)
train_label = tf.constant(train_label)

# generate a list of 2D data set arrays
data_3D = []
for file in dataset1:
    data_file = open(os.path.join(data_path1, file))
    data_3D.append(np.genfromtxt(data_file, delimiter=","))
for file in dataset2:
    data_file = open(os.path.join(data_path2, file))
    data_3D.append(np.genfromtxt(data_file, delimiter=","))
for file in dataset3:
    data_file = open(os.path.join(data_path3, file))
    data_3D.append(np.genfromtxt(data_file, delimiter=","))
for file in dataset4:
    data_file = open(os.path.join(data_path4, file))
    data_3D.append(np.genfromtxt(data_file, delimiter=","))

# generate a 3D data array and convert to a rank-3 tensor
data_3D = np.array(data_3D)
train_data = tf.convert_to_tensor(data_3D, tf.int16)

# data_num X 16 X 16
print(train_data.shape)
