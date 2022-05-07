import tensorflow as tf
tf.enable_eager_execution()



def unique():
	"""
		args
		x: tensor
		out_idx: an optional tf.DType from: tf.int32, tf.int64. Defaults to tf.int32
		name:
		returns
		y: a tensor
		idx: a tensor of type out_idx
	"""
	x = tf.constant([1,1,2,4,4,4,7,8,8])
	y, idx = tf.unique(x)
	print(y)
	print(idx)




if __name__=='__main__':
	unique()
