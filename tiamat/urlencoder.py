import random
from base64 import urlsafe_b64encode, urlsafe_b64decode

from django.conf import settings


ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


class URLEncoder(object):
    def __init__(self, secret, alphabet=ALPHABET, noise_length=12):
        self.secret = secret
        self.alphabet = alphabet
        self.noise_length = noise_length

    @staticmethod
    def xor(str1, str2):
        return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2))

    def noise(self, length):
        return ''.join([random.choice(self.alphabet) for i in range(length)])

    def encode(self, string):
        string = self.noise(self.noise_length) + string
        return urlsafe_b64encode(
            self.xor(string, self.secret)
        ).replace('=', '')

    def encode_id(self, id):
        return self.encode(str(id))

    def decode(self, string):
        if len(string) % 4:
            add = (4 - len(string) % 4) * '='
        else:
            add = ''
        return self.xor(
            urlsafe_b64decode(str(string + add)), self.secret
        )[self.noise_length:]

    def decode_id(self, string):
        return int(self.decode(string))


# Set URL_ENCODER_KEY in settings
# Make sure it is different to the SECRET_KEY setting
encoder = URLEncoder(settings.URL_ENCODER_KEY)
