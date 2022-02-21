import tensorflow as tf
tf.enable_eager_execution()


def constant():
	'''
		args
		value: a constant value (or list)
		dtype: the type of the elements
		shape: dimensions of tensor
		name: name for the tensor
		returns
		a constant tensor
	'''
	# if shape is set, the value is reshaped to match. Scalars are expanded to fill the shape
	#a = tf.constant(-1, dtype=tf.float32, shape=(3,1))
	a = tf.constant([[-1],[1],[0]])
	print(a)
	print(tf.transpose(a))
	t = a - tf.transpose(a)
	print(t)


if __name__=='__main__':
	constant()
