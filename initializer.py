import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def initializer():
	'''
		random_normal_initializer
		random_uniform_initializer
	'''
	tf.random_normal_initializer(
		mean=0.0, stddev=0.05, seed=None)
	
	tf.random_uniform_initializer(
		minval=-0.05, maxval=0.05, seed=None)



if __name__=='__main__':
	initializer()
