import socket

s = socket.socket()
print("socket suksess")

port = 4067

s.bind(('', port))
print("socket berhasil di binding ke" , port)

s.listen(5)
print("socket is listening")

while True:
    c, addr = s. accept()
    print ('got connection from', addr)

    c.send(b'thank you for connection')

    c.close()
