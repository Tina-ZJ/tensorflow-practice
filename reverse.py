import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def reverse():
	'''
		args
		tensor: a tensor
		axis: a tensor, 1-D, which dimensions to reverse
		name: a name for operation
		returns
		a tensor, has the same type as tensor
	'''
	a = [[3,4,5],[1,2,2]]
	r = tf.reverse(a,axis=[0])
	print(r)
	r = tf.reverse(a,axis=[1])
	print(r)




if __name__=='__main__':
	reverse()
