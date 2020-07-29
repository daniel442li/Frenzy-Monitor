import pymongo
import requests
import json
from discord_webhooks import DiscordWebhooks
import datetime
from datetime import timedelta 
import time

webhooks = ['https://discordapp.com/api/webhooks/649033400228773908/nptrpL3C3plQGZ52vwFw6PHs5PBjy8E2pAwmUA-jXVM_FNnr_B8SERTfYWvXDUsoGW_w', 'https://discordapp.com/api/webhooks/716398429995270174/H3mAVClDg6gEnsjNipNe4hsePPwHx37UYIR9b5PFDFf8-jKrXkP8rOEQ5ipMjSRMmEdB', 'https://discordapp.com/api/webhooks/724822916331733032/PD1NKLSagHSMBs9ELwZV7u8cYFW8L9Gp3BWKHMiAGS2DRE2gWM7xWetiDxs-09n-BqIZ']


while True:
    myclient = pymongo.MongoClient("mongodb://daniel442li:KANQzahn5dF3VzZ@cluster0-shard-00-00-jq2na.mongodb.net:27017,cluster0-shard-00-01-jq2na.mongodb.net:27017,cluster0-shard-00-02-jq2na.mongodb.net:27017/<dbname>?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    database = myclient["sudufrenzy"]
    collection = database["monitor"]

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
    
    try:
        data = requests.request("GET", url, headers=headers, data = payload, allow_redirects = False)
        response = json.loads(data.text)
        flashSales = (response['flashsales'])

        for products in flashSales:
            productID = (products['id'])
            if collection.count_documents({ 'productID': productID }, limit = 1) != 0:
                pass
            else:
                for WEBHOOK_URL in webhooks:
                    webhook = DiscordWebhooks(WEBHOOK_URL)
                    title = products['title']
                    url = "https://frenzy.sale/" + products['password']
                    try:
                        image_url = (products['image_urls'][0])
                    except:
                        image_url = ''
                    price = str(products['price_range']['max'])
                    currency = str(products['shop']['currency'])
                    totPrice = price + ' ' + currency
                    start = (products['started_at'])
                    start = datetime.datetime.strptime(start,"%Y-%m-%dT%H:%M:%S.%fZ")
                    start = start - timedelta(hours = 4)
                    count = (products['products_count'])
                    shop = (products['shop']['name'])
                    shipping_message = (products['shipping_message'])
                    if start.minute == 0:
                        minute = '00'
                    else:
                        minute = start.minute
                    if start.second == 0:
                        second = '00'
                    else:
                        second = start.minute
                    start = (f'{start.month}/{start.day}/{start.year}, {start.hour}:{minute}:{second} EST')

                    webhook.set_content(title=title, url=url)
                    webhook.set_thumbnail(url=image_url)
                    webhook.add_field(name="Price:", value=totPrice)
                    webhook.add_field(name="Store:", value=shop)
                    webhook.add_field(name="Item Count:", value=count)
                    webhook.add_field(name="Shipping", value = shipping_message)
                    webhook.add_field(name="Release Date:", value=start)
                    webhook.set_footer(icon_url = 'http://drive.google.com/uc?id=16ZsNOlvQmwI2rwjA0vnT7Z5mLiHGMqwk', text='Powered by Sudu Frenzy')
                    webhook.send()

                mydict = {'productID': productID}
                x = collection.insert_one(mydict)
                print(f'Inserted: {productID}')
        print('Repeating')
        time.sleep(10)
    except Exception as E:
        print(E)
        time.sleep(10)

