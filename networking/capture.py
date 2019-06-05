import socket
import threading
from queue import Queue

# port scanner

print_lock = threading.Lock()

target = 'pythonprogramming.net'


def scan (port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        connection = s.connect((target, port))
        with print_lock:
            print('port ', port, "Is open!")
        
        connection.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()


# Testing 100 ports
for worker in range(1, 101):
    q.put(worker)

q.join()
























