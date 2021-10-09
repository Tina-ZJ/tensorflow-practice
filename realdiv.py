import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def realdiv():
	'''
		note: tf.2.0+ version
		args
		x : a tensor, int32,int64, float32, float64 and so on
		y : have the same type as x
		name:
		returns 
		a tensor, has the same type as x
	'''
	a = tf.realdiv(x=5.0, y=2)
	print(a)




if __name__=='__main__':
	realdiv()
