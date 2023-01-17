import signal
from pynput import keyboard

__all__ = ['idle']

class idle:
  def __init__(self,time=30):
    self.TimeOut = time
    self.repeat = 0
    self.idle = keyboard.Listener(on_press = self.pressing)
    self.idle.start()
    signal.signal(signal.SIGALRM, self.timeout)
    signal.alarm(self.TimeOut)
  def timeout(self,signum,stack):
    print("\nHai Apakah Kamu Masih disini?, yang kamu ketik sebelumnya masih tersimpan diatas, lanjutkan aja")
    self.repeat = self.repeat + 1
    if self.repeat == 3:
      exit()
    signal.alarm(0)
    signal.alarm(self.TimeOut)
  def pressing(self,key):
    self.repeat = 0
    signal.alarm(0)
    signal.alarm(self.TimeOut)
  def unused(self):
    self.idle.join()
