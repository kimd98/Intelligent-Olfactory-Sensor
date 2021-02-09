# import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

print("Using TensorFlow version %s" % tf.__version__)

# scalar/rank-0 tensor = an int32 tensor by default
rank_0_tensor = tf.constant(4)
print(rank_0_tensor)

# vector/rank-1 tensor = a list of values
rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)
print(rank_1_tensor.numpy())

# matrix/rank-2 tensor = two axes
rank_2_tensor = tf.constant([[1, 2],
                             [3, 4],
                             [5, 6]], dtype=tf.float16)
print(rank_2_tensor)


