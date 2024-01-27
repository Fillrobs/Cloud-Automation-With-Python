import requests
 
# Make a GET request to Azure API
response = requests.get(
    'https://management.azure.com/subscriptions/{subscription_id}/resourceGroups?api-version=2021-04-01',
    headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
)
print(response.json())
 
