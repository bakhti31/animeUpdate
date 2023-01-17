from library import idledetector
def main():
  print("Selamat Datang, Saat ini kami baru menyajikan 2 pilihan update source")
  print("Apakah kamu ingin melihat update-an terbaru")
  update = input("(y/n) > ")
  if update == 'y':
    print("Baiklah, dari website apa yang ingin kamu lihat?")
    print("1. Anoboy")
    print('2. Bstation')
    print('3. Keduanya')
    source = int(input("(1/2/3) > "))
    if source == 1:
      print("Ini adalah update dari Anoboy")
    elif source == 2:
      print("Ini adalah update dari Bstation")
    else:
      print("Ini update-annya")

if __name__ == "__main__":
 import sys
 if len(sys.argv) > 1:
   print("Yes My Boy")
   print(sys.argv[1])
   if len(sys.argv) >2:
    print("the only acceptable args only 1, and next about it will ignored")
   exit()
 idle = idle()
 main()
