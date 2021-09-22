import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def make_ndarray():
	'''
		args
		tensor: a tensorProto
		returns
		a numpy array with the tensor contents
	'''
	a = tf.constant([[1,2,3],[4,5,6]])
	proto_tensor = tf.make_tensor_proto(a)
	b = tf.make_ndarray(proto_tensor)
	print(b)



if __name__=='__main__':
	make_ndarray()
