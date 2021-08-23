# -*-coding:utf8 -*-
import sys
import tensorflow as tf

def argmax(data):
	''' input: tensor
		dimension: which axis
	'''
	b = tf.arg_max(input=data, dimension=0)
	c = tf.keras.backend.eval(b)
	print(c)




if __name__=='__main__':
	a = [1.0, 38, 20, 45]
	argmax(a) 
