# -*-coding:utf8 -*-
import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import sys

def loss(x,y):
	return (y - x**2)**2

def gradients():
	x = tfe.Variable(2.0)
	grad = tfe.implicit_gradients(loss)
	print(loss(x,7.))
	print(grad(x,7.))

if __name__=='__main__':
	gradients()
	
