from os import write
import socket

print("\n\n     trade-messaging'e hoş geldiniz.\n\n     Bu program weapontrader tarafından yapılmıştır.\n     GitHub (daha fazla bilgi): https://github.com/weapontrader/\n\n")

open("target-ip.txt", "w").write(input("    Lütfen hedef IP girin: "))
open("my-ip.txt", "w").write(socket.gethostbyname(socket.gethostname()))
print("\n\n     Şimdi lütfen send.py'i sonra recv.py'i çalıştırın..\n\n")
