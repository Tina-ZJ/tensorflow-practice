import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def dynamic_partition():
	'''
		args
		data: a tensor
		partitions: a tensor of type int32, indices in the range [0, num_partitions]
		num_partitions: an int, the number of partitions to output
		name: a name for the operation
		returns
		a list of num_partitions tensor
	'''
	data = [10,20,30,40,50]
	partitions = [0,0,1,1,0]
	num_partitions = 2
	output1, output2 = tf.dynamic_partition(data, partitions, num_partitions)
	print(output1)
	print(output2)




if __name__=='__main__':
	dynamic_partition() 
