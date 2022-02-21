import tensorflow as tf
tf.enable_eager_execution()


def tensordot(a,b,dim):
	'''
		a: tensor of type float32 or float64
		b: tensor with the same type as a
		axes: a scalar N or a list 
		name
		when a and b are matrics (order 2), the case axes=1  or axes=[[1],[0]]is equivalent to matix multiplication	, axes=0 gives the outer product a tensor of order 4
	'''
	c = tf.tensordot(a,b, axes=dim)
	return c


if __name__=='__main__':
	a = tf.constant([[1.0, 2.0, 3.0],[1.0,2.0,1.0]])
	b = tf.constant([[1.0, 3.0, 4.0],[3.0,1.0,1.0],[3.0,1.0,1.0]])
	print(tensordot(a,b,1))

