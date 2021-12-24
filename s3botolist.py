from secrets import access_key, secret_access_key
import boto3
import os

client = boto3.client('s3',
                        aws_access_key_id = access_key,
                        aws_secret_access_key = secret_access_key)


# s3 = boto3.resource('s3', 
#                         aws_access_key_id = access_key,
#                         aws_secret_access_key = secret_access_key)
# for bucket in s3.buckets.all():
#   print(bucket.name)


response = client.list_buckets()

print(response)