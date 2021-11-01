import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()





def switch_case():
	'''
		args
		branch_index: an int tensor specifying which of branch_fns should be executed
		branch_fns: a dict mapping ints to callables
		default: optional callable that returns a structure of tensors
		name
		returns
		
	'''
	def f1(): return tf.constant(17)
	def f2(): return tf.constant(31)
	def f3(): return tf.constant(-1)
	index = tf.constant(0)
	index2 = tf.constant(1)
	index3 = tf.constant(2)
	r = tf.switch_case(index, branch_fns={0: f1, 1: f2}, default=f3)
	print(r)
	r = tf.switch_case(index2, branch_fns={0: f1, 1: f2}, default=f3)
	print(r)
	r = tf.switch_case(index3, branch_fns={0: f1, 1: f2}, default=f3)
	print(r)
	r = tf.switch_case(index, branch_fns={0: f1, 1: f2}, default=f3)
	print(r)



if __name__=='__main__':
	switch_case()
