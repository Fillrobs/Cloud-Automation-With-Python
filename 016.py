import boto3
 
# Create an S3 client
s3 = boto3.client('s3')
 
# List buckets
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f"Bucket Name: {bucket['Name']}")
 
