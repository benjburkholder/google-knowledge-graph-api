"""Python client calling Knowledge Graph Search API."""
import json
import urllib.parse
import requests

print('Knowledge Graph API')
api_key = open('api-key.txt').read()
while True:
    query = input('Enter query: ')
    querynum = input('How many results do you want? (Number): ')
    queryDesc = input('Return Knowledge Graph description? (Y/N): ')
    typequestion = input('Add entity filter? (Y/N): ')
    if typequestion == 'Y':
        print('Check Schema.org for list of entity "types": https://schema.org/docs/schemas.html')
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

    url = f'{service_url}?{urllib.parse.urlencode(params)}'
    response = json.loads(urllib.request.urlopen(url).read())
    print(f'Query: {query}' + '\n')

    try:
        for element in response['itemListElement']:
            if queryDesc == 'Y':
                print(element['result']['name'] + ' (ID: ' + element['result']['@id'] + ')' + ' (' + str(element['resultScore']) + ')' + ' Description: ' + element['result']['detailedDescription']['articleBody'])
            else:
                print(element['result']['name'] + ' (ID: ' + element['result']['@id'] + ')' + ' (' + str(element['resultScore']) + ')')
    except KeyError:
        print('<Error: Name not found>')

    print('')
    savefiles = input('Save files locally?(Y/N) ')
    if savefiles == 'Y':
        savefile = 'knowledge-graph-results.csv'
        file = open('knowledge-graph-results.csv', 'a')
        file.write(f'Query: {query}' + '\n')
        try:
            for element in response['itemListElement']:
                if queryDesc == 'Y':
                    file.write(element['result']['name'] + ' (ID: ' + element['result']['@id'] + ')' + ' (' + str(element['resultScore']) + ')' + ' Description: ' + element['result']['detailedDescription']['articleBody'] + '\n')
                else: 
                    file.write(element['result']['name'] + ' (ID: ' + element['result']['@id'] + ')' + ' (' + str(element['resultScore']) + ')' + '\n')
        except KeyError:
            print('')
    if savefiles == 'Y':
        print(f'Success. Results saved locally at {savefile}.')
        file.close()
    choice = input('Continue Querying?(Y/N): ')
    if choice == 'N':
        break


input()

