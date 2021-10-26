import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def split():
	'''
		args
		value: tensor to split
		num_or_size_splits: the number of splits
		axis: which axis to split
		num: specify the number of outputs
		name:
		returns
		tensor
	'''
	x = tf.Variable(tf.random.uniform([6,6], -1,1))
	b = tf.split(x, num_or_size_splits=3, axis=1)
	print(b)
	b = tf.split(x, num_or_size_splits=3, axis=0)
	print(b)



if __name__=='__main__':
	split()
