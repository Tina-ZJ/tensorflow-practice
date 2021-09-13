import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def gather():
	'''
		args
		params: tensor
		indices: index 
		axis: int32, int64 tensor, which axis in params to gather
		batch_dims: the number of batch dimensions
		name: operation name
		returns
		a tensor
	'''
	params = tf.constant([
		[0, 0, 1, 0, 2],
		[3, 0, 0, 0, 4],
		[0, 5, 0, 6, 0]])
	indices = tf.constant([
		[2,2],
		[0,1],
		[1,2]])	
	t = tf.gather(params, indices, axis=0)
	print(t)



if __name__=='__main__':
	gather()
		
