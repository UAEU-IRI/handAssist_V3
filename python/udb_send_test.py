import socket

UDP_IP = '192.168.1.10'
UDP_PORT = 80
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto('f', (UDP_IP, UDP_PORT))
