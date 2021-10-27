import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def squeeze():
	'''
		remove dimensions of size 1 from the shape of a tensor
		args
		input: tensor
		axis: list of ints, only squeezes the dimensions listed, defaults to [], squeezes all dimensions of size 1
		name:
		return
		a tensor
	'''

	# if t is a tensor of shape [1, 2, 1, 3, 1, 1]
	tf.shape(tf.squeeze(t))  # [2,3]
	tf.shape(tf.squeeze(t, [2,4])) # [1, 2, 3, 1]


	
