import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def clip_by_value():
	'''
		args
		t:  a tensor or IndexedSlices
		clip_value_min: the minimum value to clip
		clip_value_max: the maximum value to clip
		name:   a name for the operation

		returns
		a clipped tensor or indexedslices
	'''

	t = tf.constant([[-1, 0, 10],[-1, 0, 10]])
	print(t)
	clip_min = [[2],[1]]
	t2 = tf.clip_by_value(t, clip_value_min=clip_min, clip_value_max=100)
	print(t2)

if __name__=='__main__':
	clip_by_value()
