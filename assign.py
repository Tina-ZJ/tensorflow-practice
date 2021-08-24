import tensorflow as tf



def assign():
	'''
		args
		ref: tensor, should be from a Variable node
		value: tensor, the value to be assigned to the variable	
	'''	
	a = tf.Variable(tf.constant(0.0), dtype=tf.float32)
	#将8.0的值赋值给a
	t = tf.assign(a,8.0)
	c = tf.keras.backend.eval(t)
	z = tf.keras.backend.eval(a)
	print(c)
	print(z)


if __name__=='__main__':
	assign()
