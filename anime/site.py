from library import helpers
import time
"""
  Downloading Video File from zippy link
def downloadZippy(link="https://www54.zippyshare.com/v/lINUXLQG/file.html"):
    print(link)
    files = helpers.web(link,"#dl.button")
    print(files)



"""



"""
  Visiting a sites and getting the values

"""
def browse(name):
  info = {
    "anoboy":{
      "name":"anoboy", 
      "url":"http://anoboy.zone",
      "link":".home_index>a",
      "title":"h3"
    },
    "bstation":{
      "name":"bstation", 
      "url":"https://www.bilibili.tv/id/timeline",
      "link":".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text", 
      "title":""
    },
  }
  selected = helpers.web(info[name]['url'],info[name]['link'])
  results = []  
  for hyperlink in selected:
    judul = hyperlink.get_text()
    if info[name]['title'] != "":
      judul = hyperlink.find(info[name]['title']).get_text()
    link  = hyperlink['href']
    last = helpers.terbaru(name+".txt")
    if(judul == last):
      return []
    helpers.tulis('a',name+".txt",judul)
    #print(f"{judul[:50]:50} | {link}")
    animation = judul,link
    results.append(animation)
  return results
  #file  = helpers.terbaru(nama+".txt")
  

"""
old code plus test
  if name == "anoboy":
    link,selector = "http://anoboy.ninja", ".home_index a .amv .amvj .ibox1 "
  elif name == "bstation":
    link,selector = "https://www.bilibili.tv/id/timeline", ".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text"
  elif name == "testing":
    link,selector = "http://anoboy.ninja", ".home_index>a "
    check = parser.web(link,selector)
    for hyperlink in check:
      judul = hyperlink.find("h3")
      link = hyperlink['href']
      print ("{:<50} >>>> {:<50} ".format( str(judul.get_text()),str(link)))
    return ""
  elif name == "test":
    link,selector = "https://www.bilibili.tv/id/timeline", ".timeline.timeline--today ul.timeline__content a.bstar-video-card__title-text"
    check = parser.web(link,selector)
    for hyperlink in check:
      judul = hyperlink
      link = hyperlink['href']
      print ("{:<103} >>>> {:<10} ".format( str(judul.get_text()),str(link)))
    return ""
"""
  
"""
  check = parser.web(link,selector)
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
"""
