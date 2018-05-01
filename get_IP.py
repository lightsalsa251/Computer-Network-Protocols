import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.google.com')
print(ip)

port = 80

s.connect((ip, port))
 
print("the socket has successfully connected to google \
on port == %s" %(ip))

# For sending data the socket library has a sendall function.
# This function allows you to send data to a server to which the socket is connected and
# server can also send data to the client using this function.
