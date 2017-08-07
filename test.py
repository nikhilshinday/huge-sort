import sys 
import boto3
import numpy as np
import tables

from utils import *

def assert_sorted(array, pageSize): 
	for i in xrange(0, array.nrows, pageSize): 
		memory_array = array[i:i+pageSize]
		assert(np.all(memory_array[:-1] <= memory_array[1:]))


def main(): 
	config = get_config('test-config.yaml') 
	input_array = get_array(config['inputArrayName'])
	output_array = get_array(config['outputArrayName'])
	assert(input_array.nrows == output_array.nrows)
	assert_sorted(output_array, config['pageSize'])



if __name__ == "__main__": 
	main() 