import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def tensor_scatter_nd_add():
	'''
		args
		tensor: a tensor
		indices: index tensor, int32, int64
		updates: a tensor
		name: optional
		returns
		a tensor
	'''
	indices = tf.constant([[4],[3],[1],[7]])
	updates = tf.constant([9, 10, 11, 12])
	tensor = tf.ones([8], dtype=tf.int32)
	updated = tf.tensor_scatter_nd_add(tensor, indices, updates)
	print(updated)


if __name__=='__main__':
	tensor_scatter_nd_add()
