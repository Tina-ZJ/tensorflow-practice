import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def stack():
	'''
		stacks a list of rank- R tensors into one rank- (R+1) tensor
		args
		values: a list of tensor with the same shape and type
		axis: an int, the axis to stack along, defaults to the first dimension
		name:
		return
		output: a stacked tensor
	'''
	
	x = tf.constant([1,4])
	y = tf.constant([2,5])
	z = tf.constant([3,6])
	m = tf.stack([x,y,z])		
	print(m)


if __name__=='__main__':
	stack()
