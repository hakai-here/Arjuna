import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime




def main(target):
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    print("\n\tPort\t\tState")
    print("-" * 34)
    t1 = datetime.now()

    

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          conx = s.connect((t_ip, port))
          with print_lock:
             print("\t{}\t\topen".format(port))
             discovered_ports.append(str(port))
          conx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 10000):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("\n","[duration {}] Portscan completed".format(str(total)),"\n")
