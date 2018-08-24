# _*_ coding: utf-8 _*_
from multiprocessing import Process, Queue
import threading
import subprocess

local_var = threading.local()

def sub_input():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

def pro_write(q):
    method = local_var.methodname
    print("Begin to %s:" % method)
    for item in ["A", "B", "C"]:
        print("Put {} to the queue:".format(item))
        q.put(item)
    print("Write done.")

def pro_read(q):
    method = local_var.methodname
    print("Begin to %s:" % method)
    value = q.get()
    print("Get the value: %s" % value)

def call_method(q):
    local_var.methodname = "write"
    pro_write(q)

if __name__ == '__main__':
    q = Queue()
    local_var.methodname = "write"
    pw = threading.Thread(target=call_method, args=(q, ), name="a")
    """ local_var.methodname = "read"
    pr = threading.Thread(target=call_method, args=(q, ), name="b") """
    pw.start()
    # pr.start()
    pw.join()
    # pr.join()