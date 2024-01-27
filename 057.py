# CloudBolt CMP API calls for deploying applications across on-premises and public cloud environments
 
def deploy_hybrid_application(application_name, on_premises_servers, public_cloud_instances):
    # Deploy application on on-premises servers
    deploy_on_premises(application_name, on_premises_servers)
 
    # Deploy application on public cloud instances
    deploy_public_cloud(application_name, public_cloud_instances)
 
# Function to deploy application on on-premises servers
def deploy_on_premises(application_name, on_premises_servers):
    # Use CloudBolt CMP API to initiate the deployment on on-premises servers
    # ...
 
# Function to deploy application on public cloud instances
def deploy_public_cloud(application_name, public_cloud_instances):
    # Use CloudBolt CMP API to initiate the deployment on public cloud instances
    # ...
 
# Example usage
deploy_hybrid_application("ExampleApp", on_premises_servers=["OnPremServer1", "OnPremServer2"], public_cloud_instances=["AWS-Instance1", "Azure-Instance1"])
