"""Python client calling Knowledge Graph Search API."""
import json
import urllib.parse
import requests

api_key = open('api-key.txt').read()
query = input('Enter query: ')
querynum = input('How many results do you want? (Number): ')
typequestion = input('Add entity filter? (Y/N): ')
if typequestion == 'Y':
    kptype = input('What type of entity do you want? ')

service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': str(query),
    'limit': int(querynum),
    'indent': True,
    'key': api_key,
}

if typequestion == 'Y':
    params['types'] = kptype

print(params)

url = f'{service_url}?{urllib.parse.urlencode(params)}'
response = json.loads(urllib.request.urlopen(url).read())
print(f'Query: {query}' + '\n')
for element in response['itemListElement']:
  print(element['result']['name'] + ' (' + str(element['resultScore']) + ')')

print('')
savefiles = input('Save files locally?(Y/N) ')
if savefiles == 'Y':
  savefile = 'knowledge-graph-results.txt'
  file = open('knowledge-graph-results.txt', 'a')
  file.write(f'Query: {query}' + '\n')
  for element in response['itemListElement']:
    (element['result']['name'] + ' (' + str(element['resultScore']) + ')')
    file.write(element['result']['name'] +
               ' (' + str(element['resultScore']) + ')' + '\n')
  print(f'Success. Results saved locally at {savefile}.')
  file.close()

input()
