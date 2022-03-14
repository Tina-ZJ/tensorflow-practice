import tensorflow as tf
tf.enable_eager_execution()



def transpose():
	"""
		args
		a: a tensor
		perm: a permutation of the dimensions of a, should be a vector
		conjugate: Optional bool
		name:
		returns
		a transposed tensor
	"""
	x = tf.constant([[[ 1, 2, 3],
					  [4, 5, 6]],
					  [[7, 8, 9],
					  [10, 11, 12]]])
	y = tf.transpose(x)
	print(y)
	z = tf.transpose(x, perm=[0,2,1])
	print(z)


if __name__=='__main__':
	transpose()
