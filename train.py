import os
import numpy as np
import tensorflow as tf

# constant data info (you may change this)
data1 = 'freshair'
data2 = 'citrus'
data3 = 'peppermint'
data4 = 'fish'
data_num = 4

# data file path
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

# lists of data labels
label1 = [data1] * len(dataset1)
label2 = [data2] * len(dataset2)
label3 = [data3] * len(dataset3)
label4 = [data4] * len(dataset4)
total_num = len(label1) + len(label2) + len(label3) + len(label4)

# convert the label list to a rank-3 tensor (1 x 1 x data_num)
train_label = label1 + label2 + label3 + label4
train_label = np.array(train_label)
train_label = np.reshape(train_label, (total_num, 1, 1))
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

# convert the 3D array to a rank-3 tensor (data_num x 16 x 16)
data_3D = np.array(data_3D)
train_feature = tf.convert_to_tensor(data_3D, tf.int16)

# combine two tensors into one dataset object
train_dataset = tf.data.Dataset.from_tensor_slices((train_feature, train_label))
print(train_feature.shape)
print(train_label.shape)
print(train_dataset.element_spec)
