import socket
import rsa
import math
import random

if __name__ == '__main__':
    server = ('127.0.0.1', 51000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51001))
    print('Client Started')

    pubkey = rsa.PublicKey
    pubkey.e = int(s.recv(32))
    pubkey.n = long(s.recv(512))
    print('Acquired public key')

    plaintext = random.randint(99, 1000)
    print('Generated random number: ' + str(plaintext))
    ciphertext = (plaintext ** 17) % 3233

    '''
    Setup Completed
    '''

    LB = 0.0
    UB = 3233
    C = str(ciphertext)
    for i in range(int(math.ceil(math.log(3233, 2)))):
        C = str(((2 ** 17) % 3233) * int(C))
        s.sendto(C, server)
        ans = s.recv(32)
        if ans == '0':
            UB = (UB + LB) / 2
        elif ans == '1':
            LB = (UB + LB) / 2

    print('Plaintext found: ' + str(int(UB)))
    s.close()
