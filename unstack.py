import tensorflow as tf
tf.enable_eager_execution()

def unstack():
	'''
		args:
		value: a rank R>0 tensor
		num: in int, the length of the dimension axis
		axis: an int, the axis to unstack along
		name: a name for the operation
		returns:
		the list of tensor 
	'''
	x = tf.reshape(tf.range(12), (3,4))
	p, q, r = tf.unstack(x)
	print(p)
	print(q)
	print(r)



if __name__=='__main__':
	unstack()
