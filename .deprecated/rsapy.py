import rsa

if __name__ == '__main__':
    pubkey, privkey = rsa.newkeys(512)
    message = 'hello world'.encode('utf8')
    crypto = rsa.encrypt(message, pubkey)
    message = rsa.decrypt(crypto, privkey)
    print(message.decode('utf8'))
