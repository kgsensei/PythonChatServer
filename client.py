import socket
import threading
import time
import os
from colorama import init
from colorama import Fore, Back, Style
init(autoreset=True)
from win10toast import ToastNotifier
n=ToastNotifier()

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

os.system("title Epic Gamer Chat Client")
AppName = "Client.exe"
host_ser=input("HOST IP: ")
host_por=int(input("HOST PORT: "))
chat_nae=input("CHAT NAME: ")
chat_nae=chat_nae.replace("[","")
chat_nae=chat_nae.replace("]","")
if chat_nae == "DEVJ":
    chat_nae="[DEV] Jeremy"
soc=socket.socket()
soc.connect((host_ser,host_por))

def UpdateChat():
    try:
        joinmsggen = "[SERVER]: "+chat_nae+" has joined the server."
        soc.send(joinmsggen.encode("ascii"))
        while True:
            data=soc.recv(1024).decode("ascii")
            if "[SERVER]: " in data and "kick" in data:
                if data[15:] == chat_nae:
                    joinmsggen = "DISSCONECTION"
                    soc.send(joinmsggen.encode("ascii"))
                    n.show_toast(title='CHAT CLIENT', msg='A Server Admin Kicked You.', icon_path=None, duration=10, threaded=True)
                    os.system("taskkill /f /im \""+AppName+"\"")
                    print(color.RED+"Please note that because of the client you are using errors are common.")
            if "[SERVER]: " in data:
                print(color.CYAN+data)
            else:
                print(color.CYAN+data)
    except ConnectionResetError as e:
        n.show_toast(title='CHAT CLIENT', msg='Server Crashed.', icon_path=None, duration=10, threaded=True)
        os.system("taskkill /f /im \""+AppName+"\"")
        print(color.RED+"Please note that because of the client you are using errors are common.")

thread=threading.Thread(target=UpdateChat)
thread.start()
print(color.CYAN+"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
while True:
    try:
        data=input("")
        if data == "/leave":
            os._exit(1)
        elif data != "":
            data=chat_nae+": "+data
            soc.send(data.encode("ascii"))
    except KeyboardInterrupt:
        joinmsggen = "DISSCONECTION"
        soc.send(joinmsggen.encode("ascii"))
        n.show_toast(title='CHAT CLIENT', msg='Left Server.', icon_path=None, duration=10, threaded=True)
        os.system("taskkill /f /im \""+AppName+"\"")
        print(color.RED+"Please note that because of the client you are using errors are common.")
