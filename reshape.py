import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def reshape():
	'''
		args
		tensor: a tensor
		shape: a tensor types: int32, int64
		name:
		returns
		a tensor
	'''
	t1 = [[1,2,3],[4,5,6]]
	print(t1)
	print(tf.shape(t1).numpy())
	t2 = tf.reshape(t1,[6])
	print(t2)
	t3 = tf.reshape(t1,[3,2])
	print(t3)



if __name__=='__main__':
	reshape() 
