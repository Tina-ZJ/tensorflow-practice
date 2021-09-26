import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def one_hot():
	'''
		args
		indices: a tensor of indices
		depth: a scalar defining the depth of the one hot dimension
		on_value: a scalar defining the value to fill in output when indeices[j] = i, (default: 1)
		off_value: a scalar defining the value to fill in output when indices[j]!=i (default: 0)
		axis: the axis to fill
		dtype: data type of the output tensor
		name: a name for the operation
		returns
		output: the one-hot tensor
	'''
	indices = [0, 1, 2]
	depth = 3
	a = tf.one_hot(indices, depth)
	print(a)
	indices = [0, 2, -1, 1]
	a = tf.one_hot(indices, depth, on_value=5.0, off_value=0.1)
	print(a)



if __name__=='__main__':
	one_hot()
