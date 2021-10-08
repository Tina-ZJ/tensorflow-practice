import sys
import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()



def print():
	'''
		args
		*inputs: positional arguments that are the inputs to print.
		output_stream: the output stream, logging level, or file to print to.
		summarize: the first and last summarize elements within each dimension are recursively printed per tensor. if None, then the first 3 and last 3 elements to print, if set to -1, print all elements
		sep: separate the inputs, defaults to " "
		end: end character at the printed string. defaults to the newline character
		name: operation name
	'''
	tensor_a = tf.range(2)
	tensor_b = tensor_a * 2
	tf.print(tensor_a, tensor_b, output_stream=sys.stdout, sep=',')



if __name__=='__main__':
	print()
