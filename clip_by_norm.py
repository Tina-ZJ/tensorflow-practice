import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def clip_by_norm():
	'''
		args
		t ： tensor or IndexedSlices
		clip_norm : scalar tensor >0
		axes: the dimensions to use for computing the L2-norm
		name: operation name
		
		returns
		a clipped tensor or IndexedSlices
	'''
	data = tf.constant([[1, 1, 3, 3,2,1 ]], dtype=tf.float32)
	print(data)
	data = tf.clip_by_norm(data, 1.0)
	print(data)



if __name__=='__main__':
	clip_by_norm()
