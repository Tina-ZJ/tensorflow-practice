import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution() 





def is_tensor():
	'''
		args
		x: a python object to check
		returns
		True if x is a tensorflow-native type
	'''
	t = 5
	print(t)
	if not tf.is_tensor(t):
		t = tf.convert_to_tensor(t)
	print(t)
	print(t.shape)
	print(t.dtype)



if __name__=='__main__':
	is_tensor()
