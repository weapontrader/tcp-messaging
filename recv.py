import socket                
import time

s = socket.socket()          

host = open("target-ip.txt", "r").read()
port = 80

try:
    s.connect((host, port)) 

    while True:
       yanit = s.recv(1024)
       print("     " + yanit.decode("utf-8"))
       time.sleep(1000)

    s.close()

except socket.error as msg:
    print("    Bağlantı başarısız. Hata kodu:", msg)
