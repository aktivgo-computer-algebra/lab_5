class SRC:
    def __init__(self, modules: list[int]):
        self.modules = modules

    def __validate_numbers(self, a: [int], b: [int]):
        if len(a) > len(self.modules):
            raise BaseException('length A is greater then length M')
        if len(b) > len(self.modules):
            raise BaseException('length B is greater then length M')

        for i in range(0, len(self.modules)):
            if a[i] >= self.modules[i]:
                raise BaseException('A contains number equal o greater then M[i]')
            if b[i] >= self.modules[i]:
                raise BaseException('B contains number equal o greater then M[i]')

    def from_dec_to_src(self, num) -> [int]:
        return [num % m for m in self.modules]

    def from_src_to_dec(self, ) -> int:
        # TODO: implement
        return 0

    def sum(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in (0, len(self.modules) - 1):
            result.append((a[i] + b[i]) % self.modules[i])

        return result

    def diff(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in (0, len(self.modules) - 1):
            result.append((a[i] - b[i]) % self.modules[i])

        return result

    def mult(self, a: [int], b: [int]) -> [int]:
        self.__validate_numbers(a, b)

        result = []
        for i in (0, len(self.modules) - 1):
            result.append((a[i] * b[i]) % self.modules[i])

        return result
