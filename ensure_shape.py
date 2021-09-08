import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def ensure_shape():
	''' 
		args
		x : a tensor
		shape : a tensorshape for check
		name
	'''
		
	x = tf.constant([[1, 2, 3],
					[4, 5, 6]])
	print(x)
	tf.ensure_shape(x, [2,3])

if __name__=='__main__':
	ensure_shape()
