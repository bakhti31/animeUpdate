import requests
from bs4 import BeautifulSoup as bsoup
link = input("website: ")
resp = requests.get(link)
bs = bsoup(resp.content,'html.parser')
print(bs.prettify())
