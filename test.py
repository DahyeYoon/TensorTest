'''
 # Created by DahyeYoon on 5/18/16 at 15:30
 # Project Name: TensorTest
'''

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))