import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def ones_like():
	'''
		args
		input: a tensor
		dtype: a type for the returned tensor
		name: name of operation
		returns
		a tensor with all elements set to one and same shape with input
	'''
	a = tf.constant([[1,2,3],[4,5,6]])
	b = tf.ones_like(a)
	print(b)


if __name__=='__main__':
	ones_like()
