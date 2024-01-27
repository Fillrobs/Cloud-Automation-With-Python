from utilities.models.models import ConnectionInfo
import requests
 
ci = ConnectionInfo.objects.get(name="HyperV")
ipaddress = ci.ip
port = ci.port
protocol = ci.protocol
 
url = f"{protocol}://{ipaddress}:{port}/api/get_token/" auth = (ci.username, ci.password)
 
HEADERS = {'Content-Type': 'application/json'}
 
response = requests.post(url, headers=HEADERS, auth=auth, verify=False)
print(response.text)
print(response.json)
