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
  anime.site.browse("anoboy")
  anime.site.browse("bstation")
detect = library.idledetector.idle(func=inform)
#while True:
assist = anime.assistant.cli()
