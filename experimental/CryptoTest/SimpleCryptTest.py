from simplecrypt import encrypt, decrypt


class SimpleCryptTest(object):

    def printTest(self):
        print('hello world')

    def encryptTest(self):
        password = '12345678'
        message = 'hello world'

        print('password:', password)
        print('message:', message)

        ciphertext = encrypt(password, message)

        return ciphertext