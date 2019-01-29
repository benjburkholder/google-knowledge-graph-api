"""Example of Python client calling Knowledge Graph Search API."""
import json
import urllib.parse
import requests

api_key = open('api-key.txt').read()
query = input('Enter query: ')
querynum = input('How many results do you want? (Number): ')
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': str(query),
    'limit': int(querynum),
    'indent': True,
    'key': api_key,
}
url = f'{service_url}?{urllib.parse.urlencode(params)}'
response = json.loads(urllib.request.urlopen(url).read())
for element in response['itemListElement']:
  print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')

print('')
savefiles = input('Save files locally?(Y/N) ')
if savefiles == 'Y':
  file = open('knowledge-graph-results.txt', 'a')
  file.write(f'Query: {query}' + '\n')
  for element in response['itemListElement']:
    (element['result']['name'] + ' (' + str(element['resultScore']) + ')')
    file.write(element['result']['name'] +
             ' (' + str(element['resultScore']) + ')' + '\n')
  file.close()

