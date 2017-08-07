import boto3
import numpy as np
import tables 
import yaml

from utils import * 

ELEMENT_COUNT = 20000
WRITE_CHUNKS = 10

def generate_array(array_fname): 
	file = tables.open_file(array_fname, mode='w')
	array = file.create_earray(file.root, 'data', tables.FloatAtom(itemsize=4), (0,))
	for i in xrange(WRITE_CHUNKS): 
		new_array = np.random.rand(ELEMENT_COUNT/WRITE_CHUNKS)
		array.append(new_array)
		del new_array
	file.close() 


def upload_array(array_fname):
	bucket = boto3.resource('s3').bucket_name('huge-sort')
	bucket.upload_file(array_fname, array_fname)

def main(): 
	config = get_config()
	fname = config['inputArrayName']
	generate_array(fname)
	# upload_array(fname)	

if __name__ == "__main__": 
	main() 
