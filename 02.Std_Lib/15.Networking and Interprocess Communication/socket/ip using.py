import sys
import socket


ip = socket.gethostbyname('www.google.com')
print(ip)  # 172.217.167.4

#example 2
#"""""""""
# An example script to connect to Google using socket
# programming in Python

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:

    # this means could not resolve the host
    print ("there was an error resolving the host")
    sys.exit()

# connecting to the server
s.connect((host_ip, port))

print ("the socket has successfully connected to google on port == %s" % (host_ip))