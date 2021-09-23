import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def norm():
	'''
		args
		tensor : tensor float32, float64, complex64, complex128
		ord: supported values are 'fro', 'euclidean', 1, 2, np.inf
		axis: which axis to computed
		keepdims: if true, the axis indicated in axis are kept with size 1
		name: op name
	'''
	a = tf.constant([1.,2.,3.,4.])
	print(a)
	b = tf.norm(a, ord='euclidean', keepdims=True)
	print(b)


if __name__=='__main__':
	norm()
