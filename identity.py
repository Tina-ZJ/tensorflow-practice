import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def identity():
	'''
		args
		input: tensor, variable or anything that can be converted to a tensor using tf.convert_to_tensor
		name: operation name
		returns
		same type and contents as input
	'''
	a = tf.Variable(5)
	a_identity = tf.identity(a, name='identity_name')
	a.assign_add(1)
	print(a)
	# make a tensor that represents the value of that variable at the time it is called, so a_identity=5

	print(a_identity)



if __name__=='__main__':
	identity()
