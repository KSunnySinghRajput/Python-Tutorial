import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)import socket 

ip = socket.gethostbyname('www.google.com')
print ip