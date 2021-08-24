import socket

host = open("my-ip.txt", "r").read()
port = 80

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("     Soket oluşturuldu!")

    s.bind((host, port)) 
    print("     Socket port {}'e bağlandı!".format(port))

    s.listen(5)      
    print("     Soket dinleniyor...")

except socket.error as msg:
    print("     Hata! Kod: ",msg)

while True: 

   c, addr = s.accept()      
   print('     Bağlandı: ', addr)

   while True:
      message = input()
      c.send(host + message.encode('utf-8'))
      file = open("temp.txt", "w")
      file.write("SEN: " + message)
      file.close()

   c.close()
