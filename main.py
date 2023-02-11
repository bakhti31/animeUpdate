import library
import anime
import time
import os
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

action = input("type v to visit, or d to download")
if action == "d":
  download = int(input("type number of anime to download"))-1
  link = anime.link.getting(site[download][1])
  os.system(f"wget {link}")

else:
  visit = int(input("Type Number to visit"))-1
  #print(site[visit][1])
  library.helpers.visit(site[visit][1])
