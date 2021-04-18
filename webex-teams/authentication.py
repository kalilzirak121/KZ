import requests
import json

access_token = 'MGYzNGMyNGEtMzBlZS00Y2RlLWJkZTEtMzBjMmE2YjI3ZmY4ODZlN2UyZjktZmY0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
