import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def stop_gradient(x):
	'''
		args
		input: a tensor
		name: a name for the opration (optional)
		returns
		a tensor
	'''
	
	# this function for stable softmax
	z = x - tf.stop_gradient(tf.reduce_max(x))
	numerator = tf.exp(x)
	donominator = tf.reduce_sum(numerator)
	return numerator / denominator

	
