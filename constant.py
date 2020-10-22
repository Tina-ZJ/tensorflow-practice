# -*-coding:utf8 -*-
import tensorflow as tf

def constant():
	a = tf.constant([2, 2], name='a')
	b = tf.constant([[0,1],[2,3]], name='b')
	x = tf.multiply(a, b, name='mul')
	with tf.Session() as sess:
		print(sess.run(x))

if __name__=='__main__':
	constant()

