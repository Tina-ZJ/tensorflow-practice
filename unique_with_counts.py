import tensorflow as tf
tf.enable_eager_execution()




def unique_with_counts():
	x = [1,1,2,4,4,7,8,8,4]
	y, idx, count = tf.unique_with_counts(x)
	print(y)
	print(idx)
	print(count)




if __name__=='__main__':
	unique_with_counts()
