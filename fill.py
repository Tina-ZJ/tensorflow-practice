import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def fill():
	'''
		args
		dims: 1-D tensor
		value: a value to fill the returned tf.tensor
		name
		returns
		tf.tensor
	'''
	t = tf.fill([2,3],10)
	print(t)


if __name__=='__main__':
	fill()
