import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def tensor_scatter_nd_update():
	'''
		args
		tensor: tensor to copy/update
		indices: indices to update
		updates: updates to apply at the indices
		name: Optional
		returns
		a new tensor
	'''
	tensor = [0, 0, 0, 0, 0, 0, 0, 0]
	indices = [[1], [3], [4], [7]]
	updates = [9, 10, 11, 12]
	result = tf.tensor_scatter_nd_update(tensor, indices, updates)
	print(result)


if __name__=='__main__':
	tensor_scatter_nd_update()
