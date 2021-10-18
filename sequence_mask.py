import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import numpy as np


def sequence_mask():
	'''
		args
			lengths: inter tensor, all its valus <=maxlen
			maxlen: scalar integer tensor, default is the maximum value in lengths
			dtype: output type of tensor
			name:
		returns
			a mask tensor of shape lengths.shape + (maxlen,)
	'''
	data = tf.constant([1,3,2])
	a = tf.sequence_mask(data, 5)
	print(a)
	data = tf.constant([[1,3],[2,1]])
	b = tf.sequence_mask(data)
	print(b)


if __name__=='__main__':
	sequence_mask()
