#coding:utf-8 
from socket import * 
from os import *
import sys
import string
import re
from time import *
import os
music_dir=os.path.join("c:\\users\\Administrator","music")
scripts_dir="c:\\users\\Administrator"+"\\music\\scripts"
print(scripts_dir)
def find_all(name):
        print(name)
        for path,d,file in os.walk(music_dir):
            r=re.compile(r".*%s.*" %name,re.I)
            for i in file:
                rr=r.findall(i)
                if rr:
                    result=os.path.join(path,"\"%s\"" %rr[0])
                    return result
                        
while True:
    s=socket(AF_INET,SOCK_STREAM)
    s.bind(("",10087))
    s.listen(1)
    sock,addr=s.accept()
    print( "===== connect by",addr,"=====")
    sort=sock.recv(40960)
    sort=sort.decode("utf-8")
    print(sort)
    if sort:
        music=listdir(music_dir)
        scripts=listdir(scripts_dir)
        mm=1
        music1=[]
        for i in music:
            music1.append("%d.%s" %(mm,i))    
            mm=mm+1
        if find_all(sort):
            abs_path=find_all(sort)
            print(abs_path)
            cmd="start "+abs_path
            print(cmd)
            system(cmd)
            for x in scripts:
                music1.append(x)
            sock.send(str(music1).encode("utf-8"))

        else:
            data="==No Music or Cmd In Music Dir=="
            for x in scripts:
                music1.append(x)
            music1.append(data)
            sock.send(str(music1).encode("utf-8"))

    sock.close()
    s.close()

    
    
