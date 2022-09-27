import string

import rsa

if __name__ == "__main__":
    alphabet = string.ascii_lowercase
    p = 4999
    q = 4993

    rsa = rsa.RSA(alphabet, p, q)

    data = str(input("input text: "))

    encoded = rsa.encode(data)

    print("encoded: ", encoded)

    decoded = rsa.decode(encoded)

    print("decoded: ", decoded)