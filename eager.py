import tensorflow  as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def example():
	x = [[2.]]
	m = tf.matmul(x,x)
	print(m)



if __name__=='__main__':
	example()
