import math


class RSA:
    def __init__(self, alphabet: [str], p: int, q: int):
        self.alphabet = alphabet
        self.p = p
        self.q = q

        self.n = p * q
        self.f = (p - 1) * (q - 1)
        self.e = self.__calculate_e()
        self.d = self.__calculate_d()

    def __calculate_e(self) -> int:
        e = 2
        while math.gcd(e, self.f) != 1:
            e += 1
        return e

    def __calculate_d(self) -> int:
        d = 1
        while (self.e * d) % self.f != 1:
            d += 1
        return d

    def encode(self, data: str) -> list:
        result = []
        indexes = self.__get_indexes(data)
        for index in indexes:
            result.append((index ** self.e) % self.n)
        return result

    def __get_indexes(self, data: str) -> list:
        result = []
        for s in data:
            result.append(self.alphabet.index(s) + 1)
        return result

    def decode(self, encoded: list) -> str:
        result = ""
        for e in encoded:
            result += self.alphabet[(e ** self.d) % self.n - 1]
        return result
