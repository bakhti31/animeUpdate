#link.py
"""
  This file to used getting link from an updated anime
"""
from library import helpers,Downloader
from . import site
import re

def zippyshare(href):
  return href and re.compile("zippyshare.com").search(href)

def getting(link,reso="SD360P"):
  page = helpers.web(link)
  zippy = page.find_all(href=zippyshare)
  for zippylink in zippy:
    if zippylink.text == reso:
      #print(zippylink['href'])
      return Downloader.zippy(zippylink['href']) 
    #print(f"{zippylink.text} >> {zippylink['href']}")
  




if __name__ == "__main__":
  links = input("LInknya: ")
  getting(link)
