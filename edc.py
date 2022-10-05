from rsa import RSA


class EDC:
    def __init__(self, rsa: RSA):
        self.rsa = rsa

    def sign(self, data: str):
        hash = self.rsa.hash(data)
        return self.rsa.encode(hash)

    def check(self, data, cipher_hash: list):
        hash = self.rsa.hash(data)
        print("data hash:", hash)
        decoded_hash = self.rsa.decode(cipher_hash)
        print("decoded_hash:", decoded_hash)
        if hash != decoded_hash:
            raise BaseException("Данные не подлинные")
