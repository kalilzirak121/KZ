import requests
import json

access_token = 'MGYzNGMyNGEtMzBlZS00Y2RlLWJkZTEtMzBjMmE2YjI3ZmY4ODZlN2UyZjktZmY0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iYzIxM2Y2My1mNjQ5LTQ2NTktOGY1My1lZGRiMjJmZGEzMzc'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {
    'email': 'kalil.zirak@student.odisee.be'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))