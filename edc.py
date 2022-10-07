from rsa import RSA
from hash import Hash


class EDC:
    def __init__(self, hash: Hash, rsa: RSA):
        self.hash = hash
        self.rsa = rsa

    def sign(self, data: str):
        hash = self.hash.scaling(data)
        return self.rsa.encode(str(hash))

    def check(self, data, cipher_hash: list) -> bool:
        hash = self.hash.scaling(data)
        print('data hash: ', hash)
        decoded_hash = int(self.rsa.decode(cipher_hash))
        print('decoded hash: ', decoded_hash)
        return hash == decoded_hash
