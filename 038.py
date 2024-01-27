# Imperative Python Script
import requests
 
# Create a server instance
response = requests.post("https://cloudbolt-cmp/api/servers/", json={"name": "example_server", "flavor": "small", "image": "ubuntu"})
if response.status_code == 201:
    print("Server created successfully.")
else:
    print("Failed to create server. Response:", response.text)
 
# Configure server settings
response = requests.patch("https://cloudbolt-cmp/api/servers/example_server/", json={"settings": {"key": "value"}})
if response.status_code == 200:
    print("Server configured successfully.")
else:
    print("Failed to configure server. Response:", response.text)
