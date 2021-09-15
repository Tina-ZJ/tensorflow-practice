import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def get_static_value():
	'''
		args
		tensor: the tensor to be evaluated
		partial: if true, the returned numpy array is allowed to have partially evaluated values
		returns
		a numpy ndarry
	'''
	# a is a tensor
	a = tf.constant(10)
	# b is a numpy ndarray
	b = tf.get_static_value(a)
	print(a)
	print(b)


if __name__=='__main__':
	get_static_value()
