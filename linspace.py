import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def linspace():
	'''
		args
		start: a tensor, must be one of types: bfloat16, float32, float64, N-D tensor
		stop: same type and shape as start
		num: a tensor: int32, int64, 0-D tensor
		name: optional
		returns
		a tensor
	'''
	# compare with tf 1.5, tf 2.0 add axis to perform operation
	data = tf.linspace(10.0, 12.0, 3, name='linspace')
	print(data)



if __name__=='__main__':
	linspace()
