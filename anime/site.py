from library import parser,helpers
import time
"""
  Visiting a sites and getting the values

"""
def browse(name):
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
