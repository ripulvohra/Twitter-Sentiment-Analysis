import requests
url = 'http://sentiment.vivekn.com/api/text/'
import json
#enter the text in txt column
r=requests.post(url,{'txt':"she is a lovely girl"})
js=json.loads(r.text[:])
print(js['result']['sentiment'])
print(js['result']['confidence'])
