import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def shape():
	'''
		args
			input: a tensor or sparsetensor
			out_type: int32 or int64, defaults to tf.int32
			name:
		returns
			a tensor of type out_type

	'''
	a = tf.constant([[1,2,3],[4,5,6]])
	//输出一个tensor
	print(tf.shape(a))
	//输出一个tuple
	print(a.get_shape())
	//输出一个list
	print(a.get_shape().as_list())



if __name__=='__main__':
	shape()
