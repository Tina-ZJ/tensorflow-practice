import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def constant():
	'''
		args
		value: a constant value (or list)
		dtype: the type of the elements
		shape: dimensions of tensor
		name: name for the tensor
		returns
		a constant tensor
	'''
	# if shape is set, the value is reshaped to match. Scalars are expanded to fill the shape
	a = tf.constant(0, dtype=tf.float32, shape=(2,3))
	print(a)



if __name__=='__main__':
	constant()
