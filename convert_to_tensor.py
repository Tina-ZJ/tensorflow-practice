import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def convert_to_tensor():
	'''
		args
		value: an object: numpy arrays, python lists, scalars or tensor
		dtype: element type for the returned tensor
		name: optional name
	'''
	t = [[1.0,2.0],[3.0,4.0]]
	print(t)
	t2 = tf.convert_to_tensor(t, dtype=tf.float32)
	print(t2)


if __name__=='__main__':
	convert_to_tensor()
