import boto3
import numpy as np
import tables
import yaml

from utils import *

def collect_metadata(fname): 
	file = tables.open_file(array_fname)
	array = file.root
	print len(array)

def main(): 
	config = get_config() 
	fname = config['inputArrayName']
	bucket = get_bucket(config['bucketName'])
	bucket.download_file(fname, fname)
	collect_metadata(fname)

if __name__ == "__main__": 
	main() 

