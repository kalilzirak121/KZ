import requests

access_token = 'MGYzNGMyNGEtMzBlZS00Y2RlLWJkZTEtMzBjMmE2YjI3ZmY4ODZlN2UyZjktZmY0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params={'title': 'DevNet Associate Training!'}
res = requests.post(url, headers=headers, json=params)
print(res.json())