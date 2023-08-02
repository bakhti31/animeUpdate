import requests
from bs4 import BeautifulSoup

def web(link,selector):
  response = requests.get(link)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")
    return soup.select(selector)
  else:
    return false
