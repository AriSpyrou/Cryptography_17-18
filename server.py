import socket
import rsa
import math

if __name__ == '__main__':
    client = ('127.0.0.1', 51001)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51000))
    print('Server Started')

    print('Generating public and private key...')
    pubkey, privkey = rsa.newkeys(16)

    s.sendto(str(pubkey.e), client)
    s.sendto(str(pubkey.n), client)

    '''
    Setup Completed
    '''

    for i in range(int(math.ceil(math.log(3233, 2)))):
        ciphertext = s.recv(1024000)
        plaintext = (int(ciphertext) ** 413) % 3233
        ans = int(plaintext) % 2
        s.sendto(str(ans), client)

    s.close()
