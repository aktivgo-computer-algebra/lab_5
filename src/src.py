import math


class SRC:
    def __init__(self, modules: list[int]):
        self.modules = modules
        self.M = math.prod(self.modules)
        print('M =', self.M)

    def __validate_number(self, a: [int]):
        if len(a) != len(self.modules):
            raise BaseException('length of Number not equal length M')
        for i in range(len(self.modules)):
            if a[i] >= self.modules[i]:
                raise BaseException('Number contains number equal o greater then M[i]')

    def __validate_numbers(self, a: [int], b: [int]):
        self.__validate_number(a)
        self.__validate_number(b)

    def from_dec_to_src(self, num) -> [int]:
        return [num % m for m in self.modules]

    def from_src_to_dec(self, a: [int]) -> int:
        self.__validate_number(a)

        ci = []
        for i in range(len(a)):
            mi = int(self.M / self.modules[i])
            m_inv = mi % self.modules[i]
            ci.append(mi * m_inv)

        x0 = 0
        for i in range(len(a)):
            x0 += a[i] * ci[i]

        return x0 % self.M

    def sum(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in range(len(self.modules)):
            result.append((a[i] + b[i]) % self.modules[i])

        return result

    def diff(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in range(len(self.modules)):
            result.append((a[i] - b[i]) % self.modules[i])

        return result

    def mult(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in range(len(self.modules)):
            result.append((a[i] * b[i]) % self.modules[i])

        return result
