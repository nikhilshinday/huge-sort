import boto3
import os 
import tables
import yaml 

from utils import *

def get_config(fname='constants.yaml'):
	with open(fname) as fp:
		config = yaml.load(fp)
	return config

def get_bucket(bucket_name='huge-sort'): 
	return boto3.resource('s3').Bucket(name=bucket_name)

def get_array(array_fname, mode='r'): 
	file = tables.open_file(array_fname, mode)
	try:
		return file.root.data
	except: 
		return None

def download_array(array_fname):
	if os.path.basename(array_fname) not in os.listdir(os.path.dirname(array_fname)): 
		bucket = get_bucket()
		array_obj = [obj.key for obj in bucket.objects.all() if obj.key == array_fname]
		if not array_obj: 
			return None
	bucket.download_file(array_fname, array_fname)
	return get_array(array_fname)



