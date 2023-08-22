# -*- coding: utf-8 -*-

# 运行示例：
# python port_scan.py 127.0.0.1 1000-10000

import _thread as thread
import sys
from socket import *


def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        lock.acquire()
        print("Opened Port:", port)
        lock.release()


if __name__ == '__main__':
    # python3 port_scan_threads.py <host> <start_port>-<end_port>
    host = sys.argv[1]
    portstrs = sys.argv[2].split('-')

    start_port = int(portstrs[0])
    end_port = int(portstrs[1])

    target_ip = gethostbyname(host)

    lock = thread.allocate_lock()

    for port in range(start_port, end_port):
        thread.start_new_thread(tcp_test, (port,))
