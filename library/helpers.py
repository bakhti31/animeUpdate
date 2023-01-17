# helpers.py

#Menulis Dokumen
def tulis(mode,filename,text):
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

