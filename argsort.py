# -*-coding:utf8 -*-
import tensorflow as tf



def argsort(data):
	"""
		args
		values: 1-D or higher Tensor
		axis: which axis to sort, the default is -1, last axis
		direction: (ASCENDING or DESCENDING)
		stable: if True, tensor will not be re-ordered in the returned order
		name: name
	"""
	
	b = tf.argsort(data, axis=0, direction='ASCENDING', stable=True, name='idx')
	c = tf.keras.backend.eval(b)
	print(c)

if __name__=='__main__':
	data = [1, 10, 26.9, 2.8, 166.32, 62.3]
	argsort(data)
