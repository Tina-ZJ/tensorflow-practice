import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()


def slice():
	'''
		args
		input_: a tensor
		begin: an int32 or int64 tensor
		size: an int32 or int64 tensor
		name: 
		returns
		a tensor the same type as input_
	'''
	t = tf.constant([[[1,1,1], [2,2,2]],
					 [[3,3,3], [4,4,4]],
					 [[5,5,5], [6,6,6]]])

	# begin=[1,0,0]表示从input_的第1行[[3,3,3],[4,4,4]]开始，0列：[3,3,3]中的第0个位置3开始，size=[1,1,3]表示取1行[[3,3,3],[4,4,4]]，中再取1列[3,3,3]，再取3个元素[3,3,3]，所以最终结果为[3,3,3]	
	m = tf.slice(t, [1,0, 0], [1,1,3]) 
	print(m)
	# 同理上面的逻辑
	n = tf.slice(t, [1,0,0],[1,2,3])
	print(n)
	z = tf.slice(t,[1,0,0],[2,1,3])
	print(z)



if __name__=='__main__':
	slice() 
