# -*-coding:utf8 -*-
import tensorflow as tf

def main():
	x = tf.Variable(2.0)
	y = 2.0 * (x ** 3)
	z = 3.0 + y**2
	grad_z = tf.gradients(z, [x,y])
	with tf.Session() as sess:
		sess.run(x.initializer)
		print(sess.run(grad_z))

if __name__=='__main__':
	main()
