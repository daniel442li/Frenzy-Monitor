from discord_webhooks import DiscordWebhooks

WEBHOOK_URL = 'https://discordapp.com/api/webhooks/716398429995270174/H3mAVClDg6gEnsjNipNe4hsePPwHx37UYIR9b5PFDFf8-jKrXkP8rOEQ5ipMjSRMmEdB'
webhook = DiscordWebhooks(WEBHOOK_URL)

webhook.set_content(title='Welcome to Sudu Frenzy!')
webhook.set_footer(icon_url = 'http://drive.google.com/uc?id=16ZsNOlvQmwI2rwjA0vnT7Z5mLiHGMqwk', text='Sudu Frenzy Discord Bot')
webhook.send()