from socket import *

host = "192.168.1.34"

def conn_scan(host,port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((host,port))
        print(str(port) + ' open')
    except:
        print(str(port) + ' closed')

for port in range(20,81):
    conn_scan(host,port)

