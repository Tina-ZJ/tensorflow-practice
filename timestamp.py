import tensorflow as tf
tf.enable_eager_execution()


def timestamp():
	"""
		args:
		name: a name for the operation
		returns:
		a tensor of type float64
	"""
	print(tf.timestamp)



if __name__=='__main__':
	timestamp()
