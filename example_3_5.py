#!/usr/bin/env python
#-*- mode: python; coding: utf-8 -*-
# file: example_3_5.py
#    Created:       <2019/03/15 20:48:10>
#    Last Modified: <2019/03/16 20:14:47>

import tensorflow as tf

A = tf.constant([ [1, 2, 3],
                  [4, 5, 6] ])
print(A.get_shape())

x = tf.constant([1, 0, 1])
print(x.get_shape())

x = tf.expand_dims(x, 1)
print(x.get_shape())

b = tf.matmul(A, x)

sess = tf.InteractiveSession()
print('matmul result:\n {}'.format(b.eval()))
sess.close()

