import socket
import ssl
from time import time
import requests
import ftplib
import paramiko

class PortScanner:
    def __init__(self, target, min, max):
        
        self.open_port = []
        self.target = target
        self.min, self.max = min, max
    def CreateSocket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(1)
    def Start(self):
        for port in range(self.min,self.max):
            try:
                if self.socket.connect_ex((self.target, port)) == 0:
                    self.open_port.append(port)
                    self.socket.close()
                    self.CreateSocket()
            except:
                pass
    def Get_result(self):
        return self.open_port

class LegitPortScan:
    def __init__(self, target) -> None:
        self.sock = socket.socket()
        self.port = {}
        self.raw_http_payload = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % target
        self.target = target
        self.list_port = [21,22,80,443]
    def Scan(self):
        for port in self.list_port:
            self.sock = socket.socket()

            if(port == 80):
                stat = self.sock.connect_ex((self.target, port))
                print(stat)
                if(stat == 0):
                    self.port[80] = "filtered"
                    self.sock.send(self.raw_http_payload.encode())
                    self.sock.settimeout(1)
                    try:
                        response = self.sock.recv(4096)
                        self.port[80] = "open"
                    except:
                        self.port[80] = "filtered"

                    self.sock.shutdown(1)
            if(port == 443):
                self.port[443] = "closed"

                self.sock = socket.socket()
                stat = self.sock.connect_ex((self.target, 443))
                print(stat)
                if(stat == 0):
                    self.port[443] = "filtered"
                    try:
                        requests.get("https://" + self.target)

                        self.port[443] = "open"
                    except:
                        self.port[443] = "filtered"

                    self.sock.shutdown(1)
            if(port == 21):
                self.port[21] = "closed"

                self.sock = socket.socket()
                stat = self.sock.connect_ex((self.target, port))
                print(stat)
                if(stat == 0):
                    self.port[21] = "filtered"
                    try:
                        
                        ftp = ftplib.FTP(self.target, timeout=0.11, time=1)
                        self.port[21] = "open"
                        
                        ftp.quit()
                    except:
                        self.port[21] = "filtered"

                    self.sock.shutdown(1)
            if(port == 22):
                print("scanning port 22")
                self.port[22] = "close"

                if(self.sock.connect_ex((self.target, port)) == 0):
                    self.port[22] = "filtered"
                    print("filtered")
                    try:
                        self.port[22] = "open"
                        
                        client = paramiko.SSHClient()
                        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        client.connect(self.target, timeout=0.5, banner_timeout=0.5, auth_timeout=0.5)
                    except Exception as e:
                        self.port[22] = "filtered"

                        if(e == "No existing session"):
                            self.port[22] = "open"

                        if("No authentication methods" in str(e)):
                            self.port[22] = "open"
                        print(e)