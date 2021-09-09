import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def eye():
	'''
		args
		num_rows: int32
		num_columns: int32
		batch_shape: a list or tuple of python or 1-D int 32 tensor
		dtype:
		name:
		returns
		a tensor of shape batch_shape + [num_rows, num_columns]
	'''
	t = tf.eye(2,3,[4])
	print(t)




if __name__=='__main__':
	eye()
