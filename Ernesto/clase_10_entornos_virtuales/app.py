import requests

res = requests.get ("https://facebook.com/")
print (res.status_code)
