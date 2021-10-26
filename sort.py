import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def sort():
	'''
		args
		values: numeric tensor
		axis: which axis to sort
		direction: ASCENDING or DESCENDING
		name:
		returns
		tensor
	'''
	a = [1, 10, 26.9, 2.8]
	b = tf.sort(a)
	print(b)
	mat = [[3,2,1],
		   [2, 1, 3],
		   [1, 3, 2]]
	b = tf.sort(mat, axis=-1, direction='ASCENDING')
	print(b)
	b = tf.sort(mat, axis=0, direction='DESCENDING')
	print(b)
	b = tf.sort(mat, axis=1, direction='DESCENDING')
	print(b)


if __name__=='__main__':
	sort()
