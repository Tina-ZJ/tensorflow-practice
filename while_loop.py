# -*-coding:utf8 -*-
import tensorflow as tf
tf.compat.v1.enable_eager_execution()
import sys


def gradients():
	x = tf.Variable(2.0)
	z = tf.Variable(2.0)
	with tf.GradientTape() as tape:
		y =5- x**2 +z
		loop_vars = [
			tf.constant(0, tf.int32),
			tf.TensorArray(tf.float32, size=4),]
		_, jacobian = tf.while_loop(
			lambda j, _: j < 4,
			lambda j, result: (j + 1, result.write(j, tape.gradient(y, x))), loop_vars)
		print(jacobian)

		print(type(jacobian))	
		print(jacobian.stack())

def while_loop():
	i = tf.constant(0)
	c = lambda i: tf.less(i, 10)
	b = lambda i: (tf.add(i, 1), )
	r = tf.while_loop(c, b, [i])
	print(i)
	print(c)
	print(b)
	print(r)

if __name__=='__main__':
	#gradients()
	while_loop()	
