import string

from encryption.rsa import RSA
from hashing.scaling import ScalingHash
from encryption.edc import EDC

if __name__ == "__main__":
    alphabet = string.digits + string.ascii_lowercase
    p = 7  # 4999
    q = 13  # 4993

    rsa = RSA(alphabet, p, q)

    data = str(input('input text: '))

    encoded = rsa.encode(data)

    print('encoded: ', encoded)

    decoded = rsa.decode(encoded)

    print('decoded: ', decoded)

    hash = ScalingHash(alphabet, 2, 2, 10000)
    edc = EDC(hash, rsa)

    cipher_hash = edc.sign(data)

    print('\ncipher hash: ', cipher_hash)

    res = edc.check(data, cipher_hash)
    if res:
        print('Данные подлинные')
    else:
        print('Данные не подлинные')

    data = data[len(data) - 1:] + data[1:len(data) - 1] + data[:1]
    print('\nnew data: ', data)

    res = edc.check(data, cipher_hash)
    if res:
        print('Данные подлинные')
    else:
        print('Данные не подлинные')
