from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.resource import ResourceManagementClient
 
def provision_azure_resources():
    # Azure credentials and subscription ID
    subscription_id = 'your_subscription_id'
    credential = DefaultAzureCredential()
 
    # Create a resource group
    resource_client = ResourceManagementClient(credential, subscription_id)
    resource_client.resource_groups.create_or_update('my-azure-resource-group', {'location': 'eastus'})
 
    # Create a virtual machine
    compute_client = ComputeManagementClient(credential, subscription_id)
    compute_client.virtual_machines.create_or_update('my-azure-vm', 'my-azure-resource-group', {
        'location': 'eastus',
        'os_profile': {
            'computer_name': 'my-azure-vm',
            'admin_username': 'adminuser',
            'admin_password': 'Password123!'
        },
        'hardware_profile': {
            'vm_size': 'Standard_DS1_v2'
        },
        'storage_profile': {
            'image_reference': {
                'publisher': 'MicrosoftWindowsServer',
                'offer': 'WindowsServer',
                'sku': '2019-Datacenter',
                'version': 'latest'
            }
        }
    })
 
# Example usage
provision_azure_resources()
