import random, string, re, uuid

class KeyGenerator(object):

    def generateKey(self, size):
        return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits + '!@#$%^&*()') for _ in range(size))

    def gettingMacAddress(self):
        return ':'.join(re.findall('..', '%012x' % uuid.getnode()))