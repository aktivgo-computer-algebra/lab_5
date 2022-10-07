class ScalingHash:
    def __init__(self, alphabet: [str], a: int, b: int, m: int):
        self.alphabet = alphabet
        self.a = a
        self.b = b
        self.m = m

    def hash(self, data: str) -> int:
        t0 = (self.a * self.alphabet.index(data[0]) + self.b) % self.m
        result = self.alphabet.index(data[0]) ^ t0

        for s in data:
            t = (self.a * t0 + self.b) % self.m
            result = result ^ self.alphabet.index(s) ^ t
            t0 = t

        return result
