# helpers.py
import requests
from bs4 import BeautifulSoup

def web(link,selector=""):
  """
  return BeautifulSoup with selected tags
    Parameters :
      link(str): a Link URL of the website
      selector(str): A Css Selector to selecting the tags

  Usage:
    >>> web("https://google.com","div>a[href=https://policies.google.com/privacy]]")
    'Privacy'

      
  """
  #Mengolah html dari website tujuan untuk mendapatkan tag yang dipilih
  response = requests.get(link)
  if response.status_code == 200:
    soup = BeautifulSoup(response.content,"html.parser")
    if selector == "":
      return soup
    return soup.select(selector)
  else:
    return false

#Menulis Dokumen
def tulis(mode,filename,text):
  filename = ''.join(["docs/",filename])
  print(text,file=open(filename,mode))

#Membaca Dokumen
def terbaru(filename, full=False):
  filename = ''.join(["docs/",filename])#Mengubah alamat file kedalam folder docs
  if full == True: #fungsi untuk mengembalikan keseluruhan teks
    f = open(filename)
    return f.read()
  with open(filename, 'r') as f: #fungsi untuk mengembalikan teks yang diinginkan
    f.readline()#Melewati baris pertama
    return f.readline() #untuk mendapatkan baris kedua

def visit(link):
  import os
  os.system("xdg-open "+link)#khusus linux untuk membuka link website dari terminal
