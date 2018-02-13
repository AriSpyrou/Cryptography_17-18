import socket
import rsa
import math
import random
import sys

if __name__ == '__main__':
    server = ('127.0.0.1', 51000)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51001))
    print('Client Started')

    pubkey = rsa.PublicKey
    pubkey.e = int(s.recv(5))
    pubkey.n = long(s.recv(5))
    print('Acquired public key')

    plaintext = random.randint(99, 1000)
    print('Generated random number: ' + str(plaintext))
    ciphertext = (plaintext ** pubkey.e) % pubkey.n  # Encryption

    '''
    Setup Completed
    '''

    LB = 0.0  # Lower Bound
    UB = pubkey.n  # Upper Bound
    C = str(ciphertext)
    for i in range(int(math.ceil(math.log(pubkey.n, 2)))):
        C = str(((2 ** pubkey.e) % pubkey.n) * int(C))  # Double the plaintext
        s.sendto(str(sys.getsizeof(C)), server)  # Speeds up computation time
        s.sendto(C, server)
        ans = s.recv(1)
        if ans == '0':
            UB = (UB + LB) / 2  # Reduce upper bound
        elif ans == '1':
            LB = (UB + LB) / 2  # Increase lower bound

    print('Plaintext found: ' + str(int(UB)))
    s.close()
