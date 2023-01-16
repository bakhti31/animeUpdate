# helpers.py
#Menulis Dokumen
def tulis(mode,filename,text):
  """
  Good Idea to make this one
  if mode =="rewrite":
    f = open(filename)
    old = f.read()
    print(text, file=open(filename,"w"))#Write New File
    print(old, file=open(filename,'a'))#And Re Write the old Line
    return "Berhasil" # To make the code below not running
  """
  filename = ''.join(["docs/",filename])
  print(text,file=open(filename,mode))

#Membaca Dokumen
def terbaru(filename, full=False):
  filename = ''.join(["docs/",filename])
  if full == True:
    f = open(filename)
    return f.read()
  with open(filename, 'r') as f:
    f.readline()
    return f.readline()


