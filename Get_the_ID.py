import requests as req
import settings, json, os
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    "X-CMC_PRO_API_KEY": settings.key,
    "Accepts" : 'application/json'
}
session = req.Session()
session.headers.update(headers)
data = session.get(url)
results = json.loads(data.text)
path = os.path.abspath(os.getcwd())
filepath = os.path.join(path, 'IDs.txt')
file = open(filepath, 'w', encoding='UTF-8')
for i in range(len(results['data'])):
    file.write(json.dumps(results['data'][i]))
    file.write('\n\n')
file.close()
