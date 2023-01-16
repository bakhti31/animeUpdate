import requests
from bs4 import BeautifulSoup
import datetime 
import time

#Ubah Data Menjadi Bentuk HTML
def website(link,cssformat):
  response = requests.get(link)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")
    return soup.select(cssformat)
  else:
    return false

#Menulis Dokumen
def tulis(mode,filename,text):
  """
  Good Idea to make this one
  if mode =="rewrite":
    f = open(filename)
    old = f.read()
    print(text, file=open(filename,"w"))#Write New File
    print(old, file=open(filename,'a'))#And Re Write the old Line
    return "Berhasil" # To make the code below not running
  """
  filename = ''.join(["docs/",filename])
  print(text,file=open(filename,mode))

#Membaca Dokumen
def terbaru(filename, full=False):
  filename = ''.join(["docs/",filename])
  if full == True:
    f = open(filename)
    return f.read()
  with open(filename, 'r') as f:
    f.readline()
    return f.readline()

#website accessing(waiting for another refactoring)
def browse(name):

  if name == "anoboy":
    link,selector = "http://anoboy.ninja", ".home_index a .amv .amvj .ibox1 "
  elif name == "bstation":
    link,selector = "https://www.bilibili.tv/id/timeline", ".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text"

  check = website(link,selector)
  print(f"Update From {name}")
  file = terbaru(name+".txt")
  news = check[0].get_text()
  #print(f"Is this same \n {file} and {news}")
  if news not in file:
    tulis("w",name+".txt",name)
    for judul in check:
      tulis("a",name+".txt",judul.get_text())
      if (judul.get_text() in file):
        break
      print(judul.get_text())
      time.sleep(.3)     
  else:
    print(f"No Update From {name}")
  print("\n")
  
while True:
    browse("anoboy")
    browse("bstation")
    print("Waiting for Next Update....")
    time.sleep(60 * 10)
