import json
import requests
url = 'https://api.github.com/some/endpoint'
payload = {'test': 'test'}

r = requests.post(url, data=json.dumps(payload))
