import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()






def repeat():
	
	'''
		note: need 2.0+ version
		args
		input: an N-dimensional Tensor
		repeats: 1-D int tensor
		axis: which axis to repeat
		name:
		returns
		a tensor which has the same shape as input
	'''
	a = tf.repeat(['a','b','c'], repeats=[3,0,2], axis=0)
	print(a)
	a = tf.repeat([[1,2],[3,4]], repeats=[2,3], axis=0)
	print(a)
	a = tf.repeat([[1,2],[3,4]], repeats=[2,3], axis=1)
	print(a)


if __name__=='__main__':
	repeat() 
