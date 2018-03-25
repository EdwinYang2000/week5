# -*- coding: utf-8 -*-

import sys
import socket
import re

p = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

#scan.py --host <host> --port <start_port>-<end_port>
def scan(target_ip, portstrs):

    if '-' in portstrs:
        portstrs = portstrs.split('-')
        start_port = int(portstrs[0])
        end_port = int(portstrs[1])
        for port in range(start_port, end_port):
            sock = socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((target_ip,port))
            if result == 0:
                print (port,'open')
            else:
                print (port, 'closed')

if __name__ == '__main__':
    if sys.args[1] != "--host" and sys.arg[3] != "--port":
        print ("Parameter Error1")
    target_ip = p.match(sys.args[2])
    if target_ip:
        scan(sys.args[2],sys.args[4])
    else:
        print("Parameter Error2")



