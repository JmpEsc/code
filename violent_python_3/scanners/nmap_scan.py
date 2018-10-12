import nmap
import argparse

from itertools import chain

def nmap_scan(host, port):
    nmap_port_scan = nmap.PortScanner()
    nmap_port_scan.scan(host, port)
    #print(host)
    #print(port)
    #print(nmap_port_scan.all_hosts())
    state=(nmap_port_scan[host]['tcp'][int(port)]['state'])
    print(host + 'tcp/' + port + ' ' + state)

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
    port_range = str(args.port)
    for port in port_range:
        nmap_scan(host, port)

if __name__ == '__main__':
    main()
