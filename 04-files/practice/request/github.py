import requests

USERNAME = 'olechkakulic'
ACCESS_KEY = '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'


def github():
    request = requests.get('https://api.github.com/user', auth=(USERNAME, ACCESS_KEY))
    data = request.json()
    return data['login']
