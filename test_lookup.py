# -*-coding:utf8 -*-
import sys
import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe
import time



def test_speed():
	# 100w embedding, high time
	embed_table = np.random.random([50000, 200])
	idx = [ i for i in range(50)]
	begin = time.time()
	embed = tf.nn.embedding_lookup(embed_table, idx)
	end = time.time()
	print(end - begin)
	embed2 = tf.gather(embed_table, idx)
	end2 = time.time()
	print(end2-end)


if __name__=='__main__':
	test_speed()	
