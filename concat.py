import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def concat():
	'''
		args
		values : a list of tensor objects or a single tensor
		axis: 0-D int32 tensor, dimension along with which to concatenate
		name: a name for the operation

		returns
		a tensor 
	'''

	t1 = [[1,2,3],[4,5,6]]
	t2 = [[7,8,9],[10,11,12]]
	t = tf.concat([t1, t2], 0)
	print(t)


if __name__=='__main__':
	concat()
