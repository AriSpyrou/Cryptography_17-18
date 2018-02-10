import socket
import rsa
import random

if __name__ == '__main__':
    server = ('127.0.0.1', 51000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51001))
    print('Client Started')

    pubkey = rsa.PublicKey
    pubkey.e = int(s.recv(128))
    pubkey.n = long(s.recv(128))
    print('Acquired public key')

    '''
    Setup Completed
    '''

    plaintext = str(random.randint(99, 1000))
    ciphertext = rsa.encrypt(plaintext, pubkey)
    s.sendto(ciphertext, server)

    s.close()
