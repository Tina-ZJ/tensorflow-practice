import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def ones():
	'''
		args
		shape: a list of integers, a tuple of integers, or a 1-D tensor of type int32
		dtype: default is tf.float32
		name: a name for the operation
		returns
		a tensor with all elements set to one(1)
	'''
	a = tf.ones([3,4], tf.int32)
	print(a)
	b = tf.ones((3,4))
	print(b)


if __name__=='__main__':
	ones()
