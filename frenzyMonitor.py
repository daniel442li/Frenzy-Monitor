import time
import json
import requests
from discord_webhooks import DiscordWebhooks

pid = '0'
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/716398429995270174/H3mAVClDg6gEnsjNipNe4hsePPwHx37UYIR9b5PFDFf8-jKrXkP8rOEQ5ipMjSRMmEdB'
webhook = DiscordWebhooks(WEBHOOK_URL)

while True:
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
    try:
        response = data.json()
        firstProduct = (response['flashsales'][0])
        if firstProduct['id'] != pid:
            pid = firstProduct['id']
            title = firstProduct['title']
            url = "https://frenzy.sale/" + firstProduct['password']
            image_url = (firstProduct['image_urls'][0])
            price = str(firstProduct['price_range']['max'])
            currency = str(firstProduct['shop']['currency'])
            totPrice = price + ' ' + currency
            start = (firstProduct['started_at'])
            start = datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M:%S.%fZ")
            start = start - timedelta(hours = 4)
            count = (firstProduct['products_count'])
            shop = (firstProduct['shop']['name'])
            shipping_message = (firstProduct['shipping_message'])
            if start.minute == 0:
                minute = '00'
            else:
                minute = start.minute
            if start.second == 0:
                second = '00'
            else:
                second = start.minute
            start = f'{start.month}/{start.day}/{start.year}, {start.hour}:{minute}:{second} EST'

            webhook.set_content(title=title, url=url)
            webhook.set_thumbnail(url=image_url)
            webhook.add_field(name="Price:", value=totPrice)
            webhook.add_field(name="Store:", value=shop)
            webhook.add_field(name="Item Count:", value=count)
            webhook.add_field(name="Shipping", value = shipping_message)
            webhook.add_field(name="Release Date:", value=start)
            webhook.set_footer(icon_url = 'http://drive.google.com/uc?id=16ZsNOlvQmwI2rwjA0vnT7Z5mLiHGMqwk', text='Powered by Sudu Frenzy')
        else:
            print("No Change")
    except:
        print("404 Error: Passing")
    time.sleep(10)

