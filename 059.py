# CloudBolt CMP API calls for optimizing costs by leveraging on-premises resources for baseline workloads
 
def optimize_costs(application_name, on_premises_servers, public_cloud_instances):
    # Monitor workload and determine if scaling down is possible
 
    if workload_below_threshold():
        # Scale down resources based on the defined conditions
        scale_down(application_name, on_premises_servers, public_cloud_instances)
 
# Function to determine if workload is below a certain threshold
def workload_below_threshold():
    # Logic to monitor workload and compare against a predefined threshold
    # ...
 
# Function to scale down resources
def scale_down(application_name, on_premises_servers, public_cloud_instances):
    # Use CloudBolt CMP API to initiate scaling down of resources
    # ...
 
# Example usage
optimize_costs("ExampleApp", on_premises_servers=["OnPremServer1", "OnPremServer2"], public_cloud_instances=["AWS-Instance1", "Azure-Instance1"])
