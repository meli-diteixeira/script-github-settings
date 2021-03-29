import json
import requests

def getVarFromFile(__locals__):
    import imp
    f = open(__locals__)
    global data
    data = imp.load_source('data', '', f)
    f.close()

getVarFromFile('$(pwd)/__locals__.py')
repo = 'mercadolibre/{0}'.format(data.repository)
branch = 'master'

r = requests.put(
    'https://api.github.com/repos/{0}/branches/{1}/protection'.format(repo, branch),
    headers = {
        'Accept': 'application/vnd.github.luke-cage-preview+json',
        'Authorization': 'Token {0}'.format(data.api_token)
    },
    json = {
        "enforce_admins": Null
    }
)
print(r.status_code)
print(r.json())