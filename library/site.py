import requests,time
import library.helpers as helpers
from bs4 import BeautifulSoup


def website(link,cssformat):
  response = requests.get(link)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")
    return soup.select(cssformat)
  else:
    return false

def browse(name):
  if name == "anoboy":
    link,selector = "http://anoboy.ninja", ".home_index a .amv .amvj .ibox1 "
  elif name == "bstation":
    link,selector = "https://www.bilibili.tv/id/timeline", ".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text"

  check = website(link,selector)
  print(f"Update From {name}")
  file = helpers.terbaru(name+".txt")
  news = check[0].get_text()
  if news not in file:
    helpers.tulis("w",name+".txt",name)
    for judul in check:
      helpers.tulis("a",name+".txt",judul.get_text())
      if (judul.get_text() in file):
        break
      print(judul.get_text())
      time.sleep(.3)
  else:
    print(f"No Update From {name}")
  print("\n")
