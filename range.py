import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def range():
	'''
		args
		start: scalar,first entry
		limit: scalar, upper limit of sequence
		delta: scalar, number that increments start, defaults to 1
		dtype: the type of the elements
		name: a name for the operation
		returns
		an 1-D tensor of type dtype
	'''

	data = tf.range(start=3, limit=18, delta=3)
	print(data)
	data = tf.range(start=3, limit=1, delta=-0.5)
	print(data)
	data = tf.range(5)
	print(data)




if __name__=='__main__':
	range()
