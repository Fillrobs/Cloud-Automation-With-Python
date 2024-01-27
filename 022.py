import boto3
 
# Create an S3 bucket, upload a file, and trigger a Lambda function
s3 = boto3.client('s3')
s3.create_bucket(Bucket='my-bucket')
with open('file.txt', 'rb') as data:
    s3.upload_fileobj(data, 'my-bucket', 'file.txt')
 
lambda_client = boto3.client('lambda')
lambda_client.invoke(FunctionName='my-function', InvocationType='Event')
