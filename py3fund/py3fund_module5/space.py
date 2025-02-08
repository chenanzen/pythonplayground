import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()
ppl_in_space = json['people']

for person in ppl_in_space:
    print(person['name'], 'is in space aboard', person['craft'])