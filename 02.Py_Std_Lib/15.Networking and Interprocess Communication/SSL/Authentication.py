import requests
from getpass import getpass
print(requests.get('https://api.github.com/user', auth=('username', getpass())))
