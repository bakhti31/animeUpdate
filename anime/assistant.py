from library.idledetector import idle
from . import site
def cli():
  print("Selamat Datang, Saat ini kami baru menyajikan 2 pilihan update source")
  print("Baiklah, dari website apa yang ingin kamu lihat?")
  print("1. Anoboy")
  print('2. Bstation')
  print('3. Keduanya')
  source = int(input("(1/2/3) > "))
  if source == 1:
    print("Ini adalah update dari Anoboy")
    site.browse("anoboy")
  elif source == 2:
    print("Ini adalah update dari Bstation")
    site.browse("bstation")
  else:
    print("Ini update-annya")
    site.browse("bstation")
    site.browse("anoboy")

if __name__ == "__main__":
 import sys
 if len(sys.argv) > 1:
   print("Yes My Boy")
   print(sys.argv[1])
   if len(sys.argv) >2:
    print("the only acceptable args only 1, and next about it will ignored")
   exit()
 idling = idle()
 cli
