import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def map_fn():

	'''
		args
		(import)
		fn:  the callable to be performed
		elems: a tensor
		fn_output_signature: the output signature of fn, Must be specified if fn's input and output signatures are different
		returns
		a tensor
	'''
	a = tf.map_fn(fn=lambda t: tf.range(t, t+3), elems=tf.constant([3, 5, 2]))
	print(a)
	# must tensorflow version 2.0
	b = tf.map_fn(fn=tf.strings.length, elems=tf.constant(["hello","moon"]),fn_output_signature=tf.int32)
	print(b)
	


if __name__=='__main__':
	map_fn()	
