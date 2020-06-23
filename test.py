import requests
import json

url = "https://frenzy.shopifyapps.com/api/flashsales/"

payload = {}
headers = {
  'authority': 'frenzy.shopifyapps.com',
  'cache-control': 'max-age=0',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'sec-fetch-site': 'none',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-user': '?1',
  'sec-fetch-dest': 'document',
  'accept-language': 'en-US,en;q=0.9',
  'if-none-match': 'W/"62640607c0903a0d9f04a2f00aacbd05"'
}

data = requests.request("GET", url, headers=headers, data = payload, allow_redirects = False)

response = json.loads(data.text)
flashSales = (response['flashsales'])

for products in flashSales:
  print(products['id'])