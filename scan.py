import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import numpy as np



def scan():
	'''
	args
		fn: the callable to be performed
		elems: a tensor or sequence of tensor
		initializer, parallel_iterations, back_prop, swap_memory, infer_shape, infer_shape, reverse, name
	returns
		a tensor
	'''

	elems = np.array([1,2,3,4,5,6])
	print(elems.shape)
	sums = tf.scan(lambda a, x: x+a, elems)
	print(sums)


if __name__=='__main__':
	scan()
