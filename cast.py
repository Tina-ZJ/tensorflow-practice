import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def cast():
	'''
		args
		x : tensor or sparsetensor or indexedslices
		dtype : the destination type
		name : a name for the operation
		returns
		same shape as x
	'''
	x = tf.constant([1.8, 2.2], dtype=tf.float32)
	print(x)
	x = tf.cast(x, tf.int32)
	print(x)


if __name__=='__main__':
	cast() 
