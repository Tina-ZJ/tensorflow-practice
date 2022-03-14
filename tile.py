import tensorflow as tf
tf.enable_eager_execution()




def tile():
	"""
		args:
		input: a tensor 1-D or higher
		multiples: a tensor, must be int32 or int64
		name: a name for the operation
		returns
		a tensor. Has the same type as input
	"""
	a = tf.constant([[1,2,3],[4,5,6]],tf.int32)
	b = tf.constant([1,2], tf.int32)
	print(tf.tile(a, b))
	c = tf.constant([2,2], tf.int32)
	print(tf.tile(a,c))



if __name__=='__main__':
	tile()	
