import argparse

from socket import *
from threading import *
from itertools import chain

stdout_lock = Semaphore(value=1)


def conn_scan(host, port):
    try:
        conn_socket = socket(AF_INET, SOCK_STREAM)
        conn_socket.connect((host, port))
        #conn_socket.send('jmpesc\r\n')
        #results = conn_socket.recv(100)
        stdout_lock.acquire()
        print('%d TCP open' % port)
        #print(str(results))
        conn_socket.close()
    except:
        stdout_lock.acquire()
        #print('%d TCP closed' % port)
    finally:
        stdout_lock.release()

def port_scan(host, port_range):
    try:
        target_ip = gethostbyname(host)
    except:
        print('Cannot resolve %s : Unkown host' % host)
        return
    try:
        target_name = gethostbyaddr(target_ip)
        print('Scan results for ' + target_name[0] + ':')
    except:
        print('Scan results for ' + target_ip + ':')
    setdefaulttimeout(1)
    for port in port_range:
        t = Thread(target=conn_scan, args=(host, int(port)))
        t.start()

def parse_range_list(rl):
    def parse_range(r):
        if len(r) == 0:
            return []
        parts = r.split("-")
        if len(parts) > 2:
            raise ValueError("Invalid range: {}".format(r))
        return range(int(parts[0]), int(parts[-1])+1)
    return sorted(set(chain.from_iterable(map(parse_range, rl.split(",")))))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="Specify target host")
    parser.add_argument("port", type=parse_range_list, help="Specify target ports.  Ports can be a range and/or comma-separated, ex. 20-25, 80,443, 110")
    args = parser.parse_args()
    host = args.host
    port_range = args.port
    port_scan(host, port_range)

if __name__ == '__main__':
    main()
