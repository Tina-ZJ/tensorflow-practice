import tensorflow as tf
tf.enable_eager_execution()



def where():
	'''
		args:
		condition: a tf.tensor of dtype bool, or any numeric dtype
		x: has a shape broadcastable with condition and y
		y: has a shape broadcastable with condition and x
		name: optional
		returns
		a tensor with same types as x and y
	'''
	a = tf.where([True, False, False, True])
	print(a)
	b = tf.where([[1,0,0],[1,0,1]]).numpy()
	print(b)
	c = tf.where([True, False, True],
				x = [[1,2,3],
					 [4,5,6],
					 [7,8,9]],
				y = [[100, 32, 34],
					 [200, 10, 34],
					 [300,23,19]]
				)

	print(c)


if __name__=='__main__':
	where()
