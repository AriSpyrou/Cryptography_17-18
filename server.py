import socket
import rsa
import binascii

if __name__ == '__main__':
    client = ('127.0.0.1', 51001)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51000))
    print('Server Started')

    print('Generating public and private key...')
    pubkey, privkey = rsa.newkeys(128)

    s.sendto(str(pubkey.e), client)
    s.sendto(str(pubkey.n), client)
    print('Public key sent to client')

    '''
    Setup Completed
    '''

    ciphertext = s.recv(128)
    plaintext = rsa.decrypt(ciphertext, privkey)
    print(plaintext)

    s.close()
