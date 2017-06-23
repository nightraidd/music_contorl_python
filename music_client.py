#coding:utf-8
from socket import *
import time ,re
while True: 
        c=socket(AF_INET,SOCK_STREAM)
        c.connect(("10.98.74.53",10087 ))
        cmd=input("请输入歌曲或者cmd:")
        cmd=cmd.encode("utf-8")
        c.send(cmd)
        result=c.recv(10240).decode("utf-8")
        result=eval(result)
        for m in  result:
                print(m)
        c.close()