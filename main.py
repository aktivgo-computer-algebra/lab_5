import string

from rsa import RSA
from edc import EDC

if __name__ == "__main__":
    alphabet = string.digits + string.ascii_lowercase
    p = 3  # 4999
    q = 7  # 4993

    rsa = RSA(alphabet, p, q)

    data = str(input("input text: "))

    encoded = rsa.encode(data)

    print("encoded:", encoded)

    decoded = rsa.decode(encoded)

    print("decoded:", decoded)

    edc = EDC(rsa)

    cipher_hash = edc.sign(data)

    print("cipher_hash:", cipher_hash)

    edc.check(data, cipher_hash)

    print("Данные подлинные")
