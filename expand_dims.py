import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def expand_dims():
	'''
		args
		input: a tensor
		axis: which dimension to expand
		name
	'''
	image = tf.zeros([10,10,3])
	print(image.shape.as_list())
	shape = tf.expand_dims(image, axis=0).shape.as_list()
	print(shape)




if __name__=='__main__':
	expand_dims()
