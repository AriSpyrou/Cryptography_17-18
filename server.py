import socket
import rsa
import math

if __name__ == '__main__':
    client = ('127.0.0.1', 51001)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', 51000))
    print('Server Started')

    print('Generating public and private key...')
    pubkey, privkey = rsa.newkeys(16)  # 16 because of computational limitations

    # Allows for the server to execute first
    s.recv(1)

    s.sendto(str(pubkey.e), client)
    s.sendto(str(pubkey.n), client)

    '''
    Setup Completed
    '''

    for i in range(int(math.ceil(math.log(pubkey.n, 2)))):  # Finishes in log2(N) steps
        size = s.recv(16)  # Speeds up computation time
        ciphertext = s.recv(int(size))
        plaintext = (int(ciphertext) ** privkey.d) % privkey.n  # Decryption
        ans = int(plaintext) % 2  # Return last bit essentially
        s.sendto(str(ans), client)

    s.close()
