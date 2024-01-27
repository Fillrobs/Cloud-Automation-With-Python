from google.cloud import storage
from google.cloud import compute_v1
 
def provision_gcp_resources():
    # GCP credentials and project ID
    project_id = 'your_project_id'
    credentials = 'path/to/your/credentials.json'
 
    # Create a Cloud Storage bucket
    storage_client = storage.Client.from_service_account_json(credentials, project=project_id)
    bucket = storage_client.bucket('my-gcp-bucket')
    bucket.create()
 
    # Create a Compute Engine instance
    compute_client = compute_v1.InstancesClient.from_service_account_json(credentials, project=project_id)
    compute_client.insert(project=project_id, zone='us-central1-a', body={
        'name': 'my-gcp-instance',
        'machineType': 'zones/us-central1-a/machineTypes/n1-standard-1',
        'disks': [{
            'boot': True,
            'initializeParams': {
                'sourceImage': 'projects/debian-cloud/global/images/family/debian-10'
            }
        }],
        'networkInterfaces': [{
            'network': 'global/networks/default'
        }]
    })
 
# Example usage
provision_gcp_resources()
