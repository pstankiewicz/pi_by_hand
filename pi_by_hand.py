PRECISION = 100


class PiCalculator(object):

    def __init__(self, precision):
        self.precision = precision

    def divide_one_by(self, b):
        divider = 1
        result = ""
        for x in range(self.precision):
            if divider // b == 0:
                divider *= 10
                result += "0"
            else:
                partial = divider // b
                divider -= partial * b
                divider *= 10
                result += str(partial)
        return "%s.%s" % (result[0], result[1:])

    def add_two_strings(self, a, b):
        assert len(a) == len(b)
        a = a[::-1]
        b = b[::-1]
        result = ''
        overflow = 0
        for i, _ in enumerate(a):
            if a[i] == '.':
                result += '.'
                continue
            r = int(a[i]) + int(b[i]) + overflow
            if r >= 10:
                overflow = r // 10
                r -= 10
            else:
                overflow = 0
            result += str(r)
        return result[::-1] if overflow == 0 else str(overflow) + result[::-1]

    def sub_two_strings(self, a, b):
        assert len(a) == len(b)
        a = a[::-1]
        b = b[::-1]
        result = ''
        overflow = 0
        for i, _ in enumerate(a):
            if a[i] == '.':
                result += '.'
                continue
            r = int(a[i]) - int(b[i]) - overflow
            if r < 0:
                overflow = 1
                r += 10
            else:
                overflow = 0
            result += str(r)
        return result[::-1]

    def multiply_string_by_four(self, a):
        a = a[::-1]
        result = ''
        overflow = 0
        for i in a:
            if i == '.':
                result += '.'
                continue
            r = int(i) * 4 + overflow
            if r >= 10:
                overflow = r // 10
                r = r - overflow * 10
            else:
                overflow = 0
            result += str(r)
        return result[::-1] if overflow == 0 else str(overflow) + result[::-1]


if __name__ == '__main__':
    ITERATIONS = 10000
    PRECISION = 100

    pi_calculator = PiCalculator(PRECISION)
    result_list = []
    for a in range(1, ITERATIONS, 2):
        result_list.append(pi_calculator.divide_one_by(a))

    result = result_list[0]
    for i, _ in enumerate(result_list, 1):
        try:
            if i % 2 != 0:
                result = pi_calculator.sub_two_strings(result, result_list[i])
            else:
                result = pi_calculator.add_two_strings(result, result_list[i])
        except IndexError:
            pass

    print(pi_calculator.multiply_string_by_four(result))
