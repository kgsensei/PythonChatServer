import socket
import threading
import time
import os
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

host_ip=input("HOST IP: ")
host_port=int(input("HOST PORT: "))
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
data="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
ser=socket.socket()
lsocArray=[]
ser.bind((host_ip,host_port))
print(color.GREEN+"Server has started {"+str(host_ip)+":"+str(host_port)+"}")

def ListenForJoin():
    global ser
    global data
    global soc
    global lsocArray
    lsoc=soc
    lsocArray.append(soc)

    while True:
        try:
            ndata=lsoc.recv(1024).decode("ascii")
            if "DISSCONECTION" in ndata:
                lsocArray.remove(lsoc)
                print(color.YELLOW+"Client has disconnected")
            else:
                data=data+"\n"+ndata
                for i in lsocArray:
                    try:
                        i.send(data.encode("ascii"))
                    except Exception:
                        lsocArray.remove(i)
                        print(color.YELLOW+"Client has disconnected")
        except ConnectionResetError as e:
            pass

def CommandBypass():
    global lsocArray
    while True:
        data=input("")
        if data != "":
            data="[SERVER]: "+data
            for i in lsocArray:
                i.send(data.encode("ascii"))
            if data == "stop":
                print(color.RED+"Stopping Server")
                time.sleep(1)
                exit()
            if "kick" in data:
                print(color.RED+"Kicked "+data[5:])

thread=threading.Thread(target=CommandBypass)
thread.start()
ser.listen()
while True:
    soc,caddr=ser.accept()
    print(color.YELLOW+"Client has connected")
    thread=threading.Thread(target=ListenForJoin)
    thread.start()
