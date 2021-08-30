import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()




def case():
	'''
		args:
		pred_fn_pairs : dict or list of paris of a boolean scalar tensor
		default: Optional callable that returns a list of tensors
	 	exclusive:
		strict:
		name:
	'''		
	x = tf.constant(30)
	y = tf.constant(11)
	f1 = lambda: tf.constant(17)
	f2 = lambda: tf.constant(23)
	r = tf.case([(tf.less(x,y),f1)], default=f2)
	print(r)



if __name__=='__main__':
	case()
