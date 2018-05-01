'''
A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.
A server has a listen() method which puts the server into listen mode.
This allows the server to listen to incoming connections.
And last a server has an accept() and close() method.
The accept method initiates a connection with the client and the close method closes the connection with the client.
'''
import socket               
 
# next create a socket object
s = socket.socket()         
print("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s.bind(('', port))        
print("socket binded to %s" %(port))
'''
Passing an empty string means that the server can listen to incoming connections from other computers as well.
If we would have passed 127.0.0.1 then it would have listened to only those calls made within the local computer.
'''

# put the socket into listening mode
s.listen(5)     
print("socket is listening")           
 
# a forever loop until we interrupt it or 
# an error occurs
while True:
 
   # Establish connection with client.
   c, addr = s.accept()     
   print('Got connection from', addr)
 
   # send a thank you message to the client. 
   c.send('Thank you for connecting')
 
   # Close the connection with the client
   c.close()
'''
5 here means that 5 connections are kept waiting if the server is busy and if a 6th socket trys to connect then the connection is refused.
'''
