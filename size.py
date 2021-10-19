import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def size():
	'''
		args
		input: a tensor or sparsetensor
		name:
		out_type: defaults to tf.int32
		returns
		a tensor of type out_type, defaults to tf.int32
	'''
	t = tf.constant([[1,2,3],[4,5,6],[8,9,0],[0,9,8],[3,3,3]])
	nums = tf.size(t)
	print(nums)

if __name__=='__main__':
	size()
