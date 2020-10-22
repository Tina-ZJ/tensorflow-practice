# -*-coding:utf8 -*-
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVRL']='2'

def add():
	a = tf.constant(2, name='a')
	b = tf.constant(3, name='b')
	x = tf.add(a,b, name='add')
	write = tf.summary.FileWriter('./graphs', tf.get_default_graph())
	with tf.Session() as sess:
		print(sess.run(x))



if __name__=='__main__':
	add()
