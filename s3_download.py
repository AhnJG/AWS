import boto3

FILE_PATH = 'image/atv_rider0001.jpg'
BUCKET_NAME = 'flxr-yolo'
KEY = 'image/atv_rider0001.jpg'

client = boto3.client('s3')
client.download_file(BUCKET_NAME, KEY, FILE_PATH)
