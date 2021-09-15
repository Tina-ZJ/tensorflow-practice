import tensorflow as tf
#import tensorflow.contrib.eager as tfe
#tfe.enable_eager_execution()



# need tensorflow 2.0 version
def get_current_name_scope():
	with tf.name_scope("outer"):
		name = tf.get_current_name_scope()
		print(name)

	with tf.name_scope("inner"):
		name = tf.get_current_name_scope()
		print(name)



if __name__=='__main__':
	get_current_name_scope()
