import requests

access_token = 'MGYzNGMyNGEtMzBlZS00Y2RlLWJkZTEtMzBjMmE2YjI3ZmY4ODZlN2UyZjktZmY0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
room_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iYzIxM2Y2My1mNjQ5LTQ2NTktOGY1My1lZGRiMjJmZGEzMzc'
personal_email = 'abdel.boumalek@student.odisee.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': personal_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())