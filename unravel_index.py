import tensorflow as tf
tf.enable_eager_execution()




def unravel_index():
	"""
		args:
		indices: a tensor
		dims: a tensor, have the same type as indices 
		name: a name for the operation
		returns:
		a tensor
	"""
	y = tf.unravel_index(indices=[2,5,7], dims=[3,3])
	print(y)


if __name__=='__main__':
	unravel_index()
