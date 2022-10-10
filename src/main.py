from src import SRC

if __name__ == "__main__":
    modules = list(map(int, input('input modules: ').split(' ')))
    src = SRC(modules)

    a = int(input('input integer number: '))
    b = int(input('input integer number: '))

    a_src = src.from_dec_to_src(a)
    b_src = src.from_dec_to_src(b)

    print('a in src =', a_src)
    print('b in src =', b_src)

    sum = src.sum(a_src, b_src)
    diff = src.diff(a_src, b_src)
    mult = src.mult(a_src, b_src)

    print('a(', a_src, ') + b(', b_src, ') =', sum, '(', str(src.from_src_to_dec(sum)), ')')
    print('a(', a_src, ') - b(', b_src, ') =', diff, '(', str(src.from_src_to_dec(diff)), ')')
    print('a(', a_src, ') * b(', b_src, ') =', mult, '(', str(src.from_src_to_dec(mult)), ')')
