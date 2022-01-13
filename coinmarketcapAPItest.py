import requests as req
import settings, json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
headers = {
    "X-CMC_PRO_API_KEY": settings.key,
    "Accepts" : 'application/json'
}

parameters = {
    'convert':'USD',
    'volume_24h_min':'1000000',
    'volume_24h_max':'10000000',
    'percent_change_24h_min':'-20',
    'percent_change_24h_max':'20',
}

session = req.Session()
session.headers.update(headers)
data = session.get(url, params=parameters)

results = json.loads(data.text) #dictionary
try:
    i = 0
    while True:
        print(results['data'][i])
        i += 1
except:
    pass
