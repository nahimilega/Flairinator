import requests
import json

url = "https://www.reddit.com/r/india/comments/cgazmw/how_do_you_get_out_of_the_situation_when_there.json"

r = requests.get(url,headers = {'User-agent': 'Analyze22 reddit22'})
resp = json.loads(r.text)

try:
    self_text = resp[0]['data']['children'][0]['data']['selftext']
except:
    self_text = ''
title = resp[0]['data']['children'][0]['data']['title']
print(title)