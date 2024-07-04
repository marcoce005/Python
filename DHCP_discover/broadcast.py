import socket
from time import sleep

interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
allips = [ip[-1][0] for ip in interfaces]
msg = 'Ciro-è-stato-qui:PHP_merda'.encode('utf-8')

print(msg.hex())

"""while True:
    for ip in allips:
        print(f'sending on {ip}')
        sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("192.168.66.179", 0))
        sock.sendto(msg, ("255.255.255.255", 5005))
        sock.close()
    #sleep(1)"""
