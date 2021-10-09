import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def rank():
	'''
		args
		input: a tensor or sparsetensor
		name:
		returns
		a tensor of type int32
	'''
	t = tf.constant([[[1,1,1],[2,2,2]], [[3,3,3],[4,4,4]]])
	t2 = tf.constant([[1,1,1],[2,2,2]])
	print(tf.rank(t))
	print(tf.rank(t2))



if __name__=='__main__':
	rank()
