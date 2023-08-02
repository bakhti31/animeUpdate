import requests
from bs4 import BeautifulSoup
import datetime 
import time

#Ubah Data Menjadi Bentuk HTML
def soup(link):
        response = requests.get(link)
        if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                return soup
        else:
                return False

#Menulis Dokumen
def tulisbaru(filename,text):
	with open(filename,'w') as f:
		f.write(text+"\n")

def tambah(filename,text):
	with open(filename,'a') as f:
		f.write(text+'\n')

#Membaca Dokumen
def terbaru(filename):
	with open(filename, 'r') as f:
		return f.readline(1)


#Website Anoboy.ninja
def anoboy():
    print("Update Dari Anoboy")
    soap = soup("http://anoboy.ninja")#Parsing Html Anoboy
    if soap != False: #Memastikan Website Ada
        for judul in soap.select(".home_index a .amv .amvj .ibox1 "): #Memilah bagian yang berisi update anime
            print(judul.get_text())
            tambah("anoboy.txt",judul.get_text())
    else:
        print(f"[{datetime.datetime.now()}] Terjadi kesalahan saat mengakses website.")

#bilibili.tv/bstation
def bstation():
  print("Update Dari BiliBili/Bstation")
  bs = soup("https://www.bilibili.tv/id/timeline")#Parsing HTML Bstation
  if bs == False:	
    print(f"[{datetime.datetime.now()}] Terjadi kesalahan saat mengakses website.")
  else:
    for judul in bs.select(".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text"):#Memilah bagian yang berisi judul
      print(judul.get_text())
      tambah("bstation.txt",judul.get_text())



while True:
    anoboy()
    time.sleep(10)
    bstation()
    print("Waiting for Next Update....")
    time.sleep(60 * 60)
=======
import library
import anime
import time

"""
while True:
    anime.site.browse("anoboy")
    anime.site.browse("bstation")
    print("Waiting for Next Update....")
    time.sleep(60 * 10)
""" 
def inform():
  print(anime.site.browse("anoboy"))
  #anime.site.browse("bstation")
detect = library.idledetector.idle(func=inform)
#while True:
#assist = anime.assistant.cli()
site = anime.site.browse("anoboy")

for index,anim in enumerate(site):
  #print(f"{link[:40]:45}> {index}")
  #print(f"{str(index)+'.'[:2]:4}{link[0][:40]:45}") 
  print(f"{str(index+1)+'.'[:2]:4}{anim[0]}")

visit = int(input("Type Number to visit"))-1
#print(site[visit][1])
library.helpers.visit(site[visit][1])
