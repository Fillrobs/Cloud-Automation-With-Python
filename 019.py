Import boto3
# Create an EC2 instance
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-xxxxxxxx',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1
)
print("EC2 instance created:", response['Instances'][0]['InstanceId'])
 
