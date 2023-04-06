import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 4067


client.connect(('192.168.0.18', port))
message = client.recv(1024)
client.close()

print(message)

