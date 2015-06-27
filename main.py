#! /usr/bin/env python3

import json, requests
import sys

url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20150627T071448Z.117dacaac1e63b79.6b1b4bb84635161fcd400dace9fb2220d6f344ef"

params = dict(
    lang = sys.argv[2],
    text = sys.argv[1]
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(data['text'][0][0:])