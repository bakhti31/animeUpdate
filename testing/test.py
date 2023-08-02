import gzip
import requests
Headers = {
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#	"Accept-Encoding":"utf-8",
	"Accept-Language":"zh-CN,zh;q=0.9"
}
response = requests.get("https://www.bilibili.tv/id/play/2072563?bstar_from=share",headers = Headers)

print(response.status_code)


info = {
    "anoboy": {
      "name":"anoboy", 
      "url":"http://anoboy.ninja",
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


tes = [
    "NInja",
    "ani",
    "ina",
    "ning",
    "teng"
]
tes2 = [
  "sun",
  "miya",
  "layla",
  "balmond",
  "nana"
]

tes12 = []
print(tes[1])
for i in range(0,5):
  animes = tes[i],tes2[i]
  tes12.append(animes)


print("this is the tes")
print(tes12)
print("looping")
for yes in tes12:
  print(yes)
