import requests

r = requests.get('https://api.wipefest.net/swagger/index.html')

r.json()