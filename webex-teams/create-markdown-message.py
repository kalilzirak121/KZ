import requests

access_token = 'MGYzNGMyNGEtMzBlZS00Y2RlLWJkZTEtMzBjMmE2YjI3ZmY4ODZlN2UyZjktZmY0_PF84_ebdf3b62-c327-4af2-8733-10d8711bb8cd'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vOTIyYjFhYzAtYTA0OC0xMWViLTliZWMtMTk5N2M2NTdhMTcx'
message = 'Hello **DevNet Associates**!!'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())