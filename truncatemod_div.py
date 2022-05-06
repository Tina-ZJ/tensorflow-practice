import tensorflow as tf
tf.enable_eager_execution()



def truncatemod_div():
	'''
		args
		x: a tensor: int32, int64, float32, float64
		y: a tensor, have the same type as x
		name: operation name
	'''
	x = [1.0,2.5,4.0]
	y = [1.0, 3.0, 2.0]
	z = tf.truncatemod(x,y)
	m = tf.truncatediv(x,y)
	print(z)
	print(m)


if __name__=='__main__':
	truncatemod_div()
