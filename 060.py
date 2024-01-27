import boto3
 
def provision_aws_resources():
    # AWS credentials and region
    aws_access_key = 'your_access_key'
    aws_secret_key = 'your_secret_key'
    aws_region = 'us-east-1'
 
    # Create an S3 bucket
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
    s3_client.create_bucket(Bucket='my-aws-bucket')
 
    # Launch an EC2 instance
    ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
    ec2_client.run_instances(ImageId='ami-12345678', InstanceType='t2.micro', MinCount=1, MaxCount=1)
 
# Example usage
provision_aws_resources()
