from bs4 import BeautifulSoup
import requests
import os
"""
  Working Zippy Downloader

url = "https://www18.zippyshare.com/v/IrtoR5oL/file.html"
response = requests.get(url)
halaman = BeautifulSoup(response.content, "html.parser")
#print(halaman)
download = halaman.find(id="dlbutton")
print("Next Sibling")
location = str(download.next_sibling.next_sibling)
print(download.next_sibling.next_sibling)
first = int(location.find("/d/"))-1
end  = int(location.find(".mp4"))+4
reuri = location[first:end]
hosts = int(url.find(".com/"))+4
newuri= url[:hosts]
print(newuri)
satu = []
for new in reuri.split("\""):
  if new.find("(")!=-1:
    openbracket = int(new.find("("))+1
    closebracket = new.find(")")
    numb = "(" + str(new[openbracket:closebracket]) + ")"
    code=eval(numb)
    satu.append(str(code))
  else:
    satu.append(new)

print(satu)
nexturi = "".join(satu)

print("New Url")
print(newuri+nexturi)

"""
def zippy(url):
  gethost = int(url.find(".com"))+4
  hosts = url[:gethost]
  response = requests.get(url)
  if response.status_code == 200:
    halaman = BeautifulSoup(response.content, "html.parser")
    downloadlink = str(halaman.find(id="dlbutton").next_sibling.next_sibling)
    morelink1 = (int(downloadlink.find("/d/"))-1)
    morelink2 = (int(downloadlink.find(".mp4"))+4)
    scripts = downloadlink[morelink1:morelink2]
    morelink = []
    for link in scripts.split("\""):
      if link.find("(") != -1:
        openbracket = int(link.find("("))
        closebracket = int(link.find(")"))+1
        numbers = str(link[openbracket:closebracket])
        morelink.append(str(eval(numbers)))
      else:
        morelink.append(str(link))
    links = "".join(morelink)
    files = hosts+links
    return files


if __name__ == "__main__":
  url  = input("Link: ")
  link = zippy(url)
  print(link)
  os.system(f"wget {link}")

