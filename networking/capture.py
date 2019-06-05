import socket




# port scanner

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = 'pythonprogramming.net'


def scan(port):
    try:
        s.connect((ip, port))
        return True

    except:
        return False


for x in range(1, 26):
    if scan(x):
        print ('Port ', x,'is open')
    else:
        print('Port',x,'is closed!')






























