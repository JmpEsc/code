from socket import *

host = "192.168.1.34"

def conn_scan(host,port_range):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((target,port_range))
        print(str(port) + ' open')
    except:
        print(str(port) + ' closed')

for port in range(20,81):
    conn_scan(host,port)

