import requests

res = requests.get ("https://www.facebook.com/")
res.raise_for_status ()

data = res.text

file = open ("facebook.html", "w", encoding="utf-8")
file.write (data)
file.close ()

print ("Información guardada en facebook.html")