from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
 
# Authenticate and create a Compute Management Client
credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)
 
# List virtual machines
vms = compute_client.virtual_machines.list_all()
for vm in vms:
    print(f"VM Name: {vm.name}")
