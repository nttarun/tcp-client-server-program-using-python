import socket
host = '127.0.0.1'
port = 6000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b"this is client side")
    data = s.recv(1024)
    print('the message received from the server side is \n {}'.format(repr(data)))