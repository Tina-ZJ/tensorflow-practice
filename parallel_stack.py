import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def parallel_stack():
	'''
		args
		values: a list of tensor objects with the same shape and type
		name:
		returns
		output: a stacked tensor with the same type as values
	'''

	x = tf.constant([1,4])
	y = tf.constant([2,5])
	z = tf.constant([3,6])
	a = tf.parallel_stack([x,y,z])
	print(a)


if __name__=='__main__':
	parallel_stack()
