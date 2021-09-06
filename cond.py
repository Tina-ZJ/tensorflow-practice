import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def cond():
	'''
		args
		pred: a scalar determining whether to return the result of true_fn or false_fn
		true_fn: be performed if pred is true
		false_fn: be performed if pred is false
		name
		returns
		tensors 
	'''

	x = tf.constant(2)
	y = tf.constant(5)
	def f1(): return tf.multiply(x, 17)
	def f2(): return tf.add(y, 23)
	r = tf.cond(tf.less(x,y), f1, f2)
	print(r)


if __name__=='__main__':
	cond()
