from cryptography.fernet import Fernet
import base64
import json

class FernetTest(object):

    token_storage = None

    def encryptionTest(self):
        print('encrypting now')
        token = base64.b64encode(Fernet.generate_key()).decode('utf-8')
        print(token)
        FernetTest.token_storage = token
        key = base64.b64decode(token)
        f = Fernet(key)
        json_string = json.dumps({'Speak': 'Hello World'})
        ciphertext = f.encrypt(json_string.encode("utf-8"))
        ciphertext_64 = base64.b64encode(ciphertext)

        return ciphertext_64
